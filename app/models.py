from . import db
from flask_login import UserMixin
from datetime import datetime
# used for password hashing
from werkzeug.security import generate_password_hash, check_password_hash
# passes user id to queries
from . import login_manager


class User(UserMixin, db.Model):
    '''
    user class model with username, passwords
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch', backref='user', lazy="dynamic")
    comments = db.relationship('Comment', backref='user', lazy="dynamic")

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Category(db.Model):
    '''
    Categories model for Pitch
    '''
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer)
    category = db.Column(db.String(255))
    # from foreign key
    pitch_id = db.relationship('Pitch', backref='category', lazy="dynamic")

    def save_category(self):
        '''
        save category models to db
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        '''
        querys database for a categories by id the returns all id
        '''
        categories = Category.query.order_by('-id').all()
        return categories

    @classmethod
    def get_category(cls, id):
        '''
        querys database for a category
        '''
        category = Category.query.filter_by(id=id).first()
        return category


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
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    comments = db.relationship('Comment', backref='pitch', lazy="dynamic")

    def save_pitch(self):
        '''
        save pitch models to db
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls, id):
        '''
        querys database for a pitch by id the returns id
        '''
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch

    @classmethod
    def get_pitches(cls):
        '''
        get all pitches from database
        '''
        pitches = Pitch.query.order_by('-id').all()
        return pitches

    @classmethod
    def get_pitched(cls, id):
        '''
        get pitch base on category id
        '''
        pitched = Pitch.query.filter_by(category_id=id).all()
        return pitched

    @classmethod
    def get_userpitch(cls, id):
        '''
        get user pitches
        '''
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches


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

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, id):
        '''
        filter comment by pitch id
        '''
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments
