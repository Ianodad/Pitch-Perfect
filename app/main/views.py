from flask import render_template

# importing main from main blueprint
from . import main
# importing Forms
from .forms import PitchForm
# importing database
from .. import db
#import models
from ..models import Pitch


@main.route('/pitch')
def index():
    title = 'Home is best'

    return render_template('index.html', title=title)


@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
def pitch():
    return render_template('pitch.html')
