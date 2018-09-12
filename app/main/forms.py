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
    pitch = TextAreaField('Your Post here', validators=[Required()])
    date = DateField('Post Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')


class CommentsForm(FlaskForm):

    '''
    comments of the pitchs
    '''
    comments = TextAreaField('comment here')
    submit = SubmitField('Comment')


class CategoryForm(FlaskForm):
    '''
    category forms that we provide
    '''
    category = StringField('Your category here')
    submit = SubmitField('Create Category')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')
