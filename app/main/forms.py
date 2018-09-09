from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required
from ..models import Pitch


class PitchForm(FlaskForm):
    '''
    Form for posting pitchs
    '''
    title = StringField('Your title here', validators=[Required()])
    Pitch = StringField('Your Post here', validators=[Required()])
    submit = SubmitField('Submit')
