from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/')
def home():
    all_dojos=Dojo.get_all_dojos()
    return render_template('dojos.html', all_dojos=all_dojos)

@app.route('/dojo/create', methods=['post'])
def add_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')

@app.route('/dojo/show/<int:id>')
def show_one_dojo(id):
    data = {
        'id' : id
    }
    one_dojo = Dojo.get_one(data)
    return render_template('dojos_show.html', one_dojo=one_dojo)
# @app.route('/dojo/show/')
# def show_one_dojo(id):
#     data = {
#         'id':id
#     }
#     all_ninjas = Ninja.get_ninjas_in_dojos(data)
#     one_dojo = Dojo.get_one(data)
#     return render_template('dojos_show.html', all_ninjas=all_ninjas, one_dojo=one_dojo)


