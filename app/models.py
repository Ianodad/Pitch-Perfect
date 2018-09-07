from . import db
from flask_login import UserMixin


# class for user input

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    # password_hash = db.Column(db.String(255))
    # posted = db.relationship('Review', backref='user', lazy="dynamic")
    # comment = db.relationship('Comment', backref='user', lazy="dynamic")

    def __repr__(self):
        return f'User {self.username}'
