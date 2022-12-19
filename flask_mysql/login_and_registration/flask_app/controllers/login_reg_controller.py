from flask import Flask, render_template, redirect, request, session
from flask_app.models.login_reg_model import User
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)





@app.route('/')
def login():
    # default home page that will show registration form or login
    if "user_id" in session:
        return redirect('login/dashboard')
    else:
        return render_template('index.html')

@app.route('/users/register', methods=['POST'])
def gather():
    if not User.validator(request.form):
        return redirect('/')
        # hashing the password here
    hashed_pass = bcrypt.generate_password_hash(request.form['password'])
        
    data = {
        **request.form,
        'password' : hashed_pass,
        'conf_pass' : hashed_pass
        #will hash confirm password also
    }
    # creating the account with hashed pass
    logged_user_id = User.new_user(data)
    # storing the users id in session to consider them logged in
    session['user_id'] = logged_user_id
    return redirect('/login/dashboard')


@app.route('/login/dashboard')
def dashboard():
    # protects dashboard if user is not logged in
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(data)
    return render_template("dashboard.html", logged_user=logged_user)

@app.route('/users/login', methods=['POST'])
def log_user():
    data = {
        'email' : request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email", 'log')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password", 'log')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/login/dashboard')
    

@app.route('/user/logout')
def logout():
    # this will delete session cookie and redirect to root route
    del session['user_id']
    return redirect('/')