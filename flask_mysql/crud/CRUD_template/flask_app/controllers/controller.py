from flask import Flask, render_template, redirect, request, session
# imports flask for flask actions
from flask_app.models.model import User
# this will import models into controller to convert raw DB data 
# USE the CLASS needed not the entire model file and 
# rename using proper naming convention
from flask_app import app
# imports init file from flask app
from flask import flash
# import flash for incorrect inputs
from flask_bcrpyt import Bcrypt
bcrypt = Bcrypt(app)
# template for bcrypt



@app.route('/')
def home():
    if 'user_id' in session:
        return redirect('/dashboard')
    # if user is already logged in redirect to dashboard
    
    return render_template('index.html')
# home page of project




# template for logins
@app.route('/users/register', methods=['POST'])
def reg_user():
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
    logged_user_id = User.create(data)
    # storing the users id in session to consider them logged in
    session['user_id'] = logged_user_id
    return redirect('/dashboard')
    
    
    
@app.route('/users/login', methods=['POST'])
def log_user():
    data = {
        'email' : request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("invalid credentials", 'log')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password'])
        flash("invalid credentials", 'log')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return render_template('/dashboard')
    
    
@app.route('/users/logout')
def log_out():
    # deleting user_id from session logs user out
    del session['user_id']
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    # protects dashboard if user is not logged in
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id':session['user_id']
    }
    logged_user = User.get_by_id(data)
    return render_template("dashboard.html", logged_user=logged_user)




# template for logins









@app.route('/project/create', methods=['POST'])
def project_create():
    # this will take in a form for insert query to DB
    if not Class_from_model(request.form):
        return redirect('/project/create')
    # this validator will check if all requirements are met, 
    # if not redirect to create page
    Class_from_model.create(request.form)
    # creates a class model from request form
    return redirect('/')