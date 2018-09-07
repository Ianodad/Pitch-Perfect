from . import db
from flask_login import UserMixin
from datetime import datetime


# class for user input

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    posts = db.relationship('Post', backref='user', lazy="dynamic")
    comments = db.relationship('Comment', backref='user', lazy="dynamic")

    # password_hash = db.Column(db.String(255))
    # posted = db.relationship('Review', backref='user', lazy="dynamic")

    def __repr__(self):
        return f'User {self.username}'


class Catergory(db.Model):
    '''
    Catergories model for post
    '''
    __tablename__ = 'categories'

    id = db.Column(db.Interger, primary_key=True)
    cat_id = db.Column(db.Integer)
    cat_name = db.Column(db.Integer)
    post_id = db.relationship('Post', backref='catergory', lazy="dynamic")


class Post(db.Model):
    '''
    Post model contain user pitch 
    '''
    __tablename__ = 'posts'

    id = db.Column(db.Interger, primary_key=True)
    Post_id = db.Column(db.Integer)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    catergory_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    comments = db.relationship('Comment', backref='post', lazy="dynamic")


class Comment(db.Model):
    '''
    Comment model containing user comments
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Interger, primary_key=True)
    comment_id = db.Column(db.Integer)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
