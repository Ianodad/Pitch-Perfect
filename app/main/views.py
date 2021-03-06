from flask import render_template, redirect, url_for, abort

# importing main from main blueprint
from . import main
# importing Forms
from .forms import PitchForm, CommentsForm, CategoryForm, UpdateProfile
# importing database
from .. import db
# import models
from ..models import Pitch, Comment, User, Category

# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm


@main.route('/')
def index():
    title = 'Home is best'
    pitchd = Pitch.get_pitches()
    # username = P
    category = Category.get_categories()
    return render_template('index.html', title=title, pitchd=pitchd, category=category)


@main.route('/pitch', methods=['GET', 'POST'])
@login_required
def pitch():
    pitch = PitchForm()
    comment = CommentsForm()

    if pitch.validate_on_submit():
        title = pitch.title.data
        pitch = pitch.pitch.data
        # date = pitch.date.data

        new_pitch = Pitch(title=title, pitch=pitch, user_id=current_user.id)
        new_pitch.save_pitch()

        return redirect(url_for('.pitch'))

    pitches = Pitch.get_pitches()
    print(pitches)
    title = 'ALL PITCHES'
    # comments = get_comment(id)
    return render_template('pitch.html', title=title, pitch=pitch, pitches=pitches, comment=comment)


@main.route('/category/<int:id>', methods=['GET', 'POST'])
@login_required
def categoryPitch(id):

    pitch = PitchForm()

    if pitch.validate_on_submit():
        title = pitch.title.data
        pitch = pitch.pitch.data
        # date = pitch.date.data

        new_pitch = Pitch(title=title, pitch=pitch,
                          user_id=current_user.id, category_id=id)
        new_pitch.save_pitch()

        return redirect(url_for('.pitch'))

    pitches = Pitch.get_pitched(id)
    print(pitches)

    category = Category.get_category(id)

    title = f'{category.category} pitch'    # comments = get_comment(id)
    return render_template('pitchCat.html', title=title, pitch=pitch, pitches=pitches)


@main.route('/commented/<int:id>', methods=['GET', 'POST'])
@login_required
def commented(id):

    this_pitch = Pitch.get_pitch(id)
    print(this_pitch.title)
    comments = CommentsForm()

    if comments.validate_on_submit():
        comment = comments.comments.data
        new_comment = Comment(comment=comment, pitch_id=id,
                              user_id=current_user.id)
        new_comment.save_comment()

        # return redirect(url_for('main.commnted'))

    pitch_comments = Comment.get_comment(id)

    title = f'{this_pitch.title} comment'
    return render_template('commented.html', pitch=this_pitch, comments=comments, pitch_comments=pitch_comments)


@main.route('/category', methods=['GET', 'POST'])
@login_required
def category():
    categoryForm = CategoryForm()

    if categoryForm.validate_on_submit():
        category = categoryForm.category.data
        new_category = Category(category=category)

        new_category.save_category()

        # return redirect(url_for('.index'))

    categories = Category.get_categories()

    return render_template('category.html', categories=categories, category=categoryForm)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)
    pitches = Pitch.get_userpitch(current_user.id)
    title = f'{current_user.username}'
    return render_template("profile/profile.html", user=user, pitches=pitches, title=title)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)
