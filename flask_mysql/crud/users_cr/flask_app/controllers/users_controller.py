from flask import Flask, render_template, redirect,request
from flask_app.models.user_model import Users
from flask_app import app


@app.route('/')
def index():
    all_users = Users.get_all()
    # all users uses class method from users_model
    return render_template('Read(All).html', all_users=all_users)

@app.route('/users/new')
def new_user_form():
    return render_template('create.html')

@app.route('/users/create', methods=['POST'])
def create_new_user():
    Users.create(request.form)
    last_user = Users.show_last()
    return redirect('/users/show/one/' + str(last_user.user_id))

@app.route('/users/show/last/')
def show_last_user():
    # class method to get last created user
    last_user = Users.show_last()
    get_user_id = last_user.user_id
    return redirect('/users/show/one/get_user_id')

@app.route('/users/show/one/<int:user_id>')
def show_one(user_id):
    data = {
        'id':user_id
    }
    one_user = Users.get_one_user(data)
    return render_template('Read(One).html', one_user=one_user)

@app.route('/users/edit/<int:user_id>')
def edit_user(user_id):
    one_user = Users.get_one_user({'id':user_id})
    return render_template('edit_user.html', one_user=one_user)

@app.route('/users/update/<int:user_id>', methods=['POST'])
def update_user_form(user_id):
    data = {
        'id':user_id,
        **request.form
    }
    Users.update_user(data)
    return redirect('/')

@app.route('/users/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        'id':user_id
    }
    Users.delete_user(data)
    return redirect('/')