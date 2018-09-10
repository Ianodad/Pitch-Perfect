from flask import render_template, redirect, url_for

# importing main from main blueprint
from . import main
# importing Forms
from .forms import PitchForm, CommentsForm
# importing database
from .. import db
# import models
from ..models import Pitch, Comment, User

# decorator that will user authentication
from flask_login import login_required, current_user
# importing wft
from flask_wtf import FlaskForm


@main.route('/')
def index():
    title = 'Home is best'

    return render_template('index.html', title=title)


@main.route('/pitch', methods=['GET', 'POST'])
def pitch():
    pitch = PitchForm()
    comment = CommentsForm()

    if pitch.validate_on_submit():
        title = pitch.title.data
        pitch = pitch.pitch.data
        # date = pitch.date.data

        new_pitch = Pitch(title=title, pitch=pitch, )
        new_pitch.save_pitch()

        return redirect(url_for('.pitch'))

    # if comment.validate_on_submit():
    #     commented = comment.comments.data

    #     new_comment = Comment(comment=commented)
    #     new_comment.save_comment()

    #     return redirect(url_for('.pitch'))

    pitches = Pitch.get_pitches()
    print(pitches)
    title = 'Pitch it here!'
    # comments = get_comment(id)
    return render_template('pitch.html', title=title, pitch=pitch, pitches=pitches, comment=comment)


@main.route('/commented/<int:id>', methods=['GET', 'POST'])
def commented(id):

    this_pitch = Pitch.get_pitch(id)
    print(this_pitch.title)
    comments = CommentsForm()

    if comments.validate_on_submit():
        comment = comments.comments.data
        new_comment = Comment(comment=comment, pitch_id=id,
                              user_id=current_user.id)
        new_comment.save_comment()

        return redirect(url_for('.pitch'))

    pitch_comments = Comment.get_comment(id)

    title = 'Pitch Perfect'
    return render_template('commented.html', pitch=this_pitch, comments=comments, pitch_comments=pitch_comments)
