from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required
from ..models import Pitch


class PitchForm(FlaskForm):
    '''
    Form for posting pitchs
    '''
    title = StringField('Your title here', validators=[Required()])
    pitch = StringField('Your Post here', validators=[Required()])
    date = DateField('Post Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')
