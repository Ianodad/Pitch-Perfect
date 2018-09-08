from . import db
from flask_login import UserMixin
from datetime import datetime


# class for user input

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    password_hash = db.Column(db.String(255))

    posts = db.relationship('Pitch', backref='user', lazy="dynamic")
    comments = db.relationship('Comment', backref='user', lazy="dynamic")

    def __repr__(self):
        return f'User {self.username}'


class Catergory(db.Model):
    '''
    Catergories model for Pitch
    '''
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer)
    cat_name = db.Column(db.String(255))
    post_id = db.relationship('Pitch', backref='catergory', lazy="dynamic")


class Pitch(db.Model):
    '''
    Post model contain user pitch
    '''
    __tablename__ = 'pitchs'

    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    # end of true feilds
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    catergory_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    comments = db.relationship('Comment', backref='pitch', lazy="dynamic")


class Comment(db.Model):
    '''
    Comment model containing user comments
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    comment_id = db.Column(db.Integer)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitchs.id"))
