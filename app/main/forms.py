from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required
from ..models import Pitch


class PitchForm(FlaskForm):
    '''
    Form for posting pitchs
    '''
    post = StringField('Your Post here', validators=[Required()])
    submit = SubmitField('Submit')
