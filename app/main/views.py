from flask import render_template

# importing main from main blueprint
from . import main


@main.route('/')
def index():
    title = 'Home is best'

    return render_template('index.html', title=title)
