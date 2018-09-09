from flask import render_template, redirect, url_for

# importing main from main blueprint
from . import main
# importing Forms
from .forms import PitchForm
# importing database
from .. import db
# import models
from ..models import Pitch


@main.route('/')
def index():
    title = 'Home is best'

    return render_template('index.html', title=title)


@main.route('/pitch', methods=['GET', 'POST'])
def pitch():
    pitch = PitchForm()

    if pitch.validate_on_submit():
        title = pitch.title.data
        pitch = pitch.pitch.data
        date = pitch.date.data

        new_pitch = Pitch(title=title, pitch=pitch, posted=date)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    pitches = Pitch.get_pitches()
    title = 'Pitch it here!'
    return render_template('pitch.html', title=title, pitch=pitch, pitches=pitches)
