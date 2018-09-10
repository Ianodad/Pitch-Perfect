from flask import render_template, redirect, url_for
# from user we are import use model
from ..models import User
# importing database form SQLalchemy
from .. import db

from . import auth
# form for registrating form
from .forms import RegistrationForm


@auth.route('/register', methods=["GET", "POST"])
def register():
    '''
    geting data from auth form registratin form
    '''
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account Details"
    return render_template('auth/register.html', registration_form=form)


@auth.route('/login')
def login():
    '''
    Login user after regisatering 
    '''
    return render_template('auth/login.html')
