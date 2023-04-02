from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('home.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('email is invalid', category="error")
        elif len(firstName) < 2:
            flash("First Name must be at least 2 characters long", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long", category="error")
        else:
            #add user to database
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha1'), password2=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("You have successfully created a new user", category="success")
            return redirect(url_for('views.home'))

    return render_template('sign_up.html')