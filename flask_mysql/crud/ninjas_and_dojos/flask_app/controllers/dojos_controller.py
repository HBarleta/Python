from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/dojo/create', methods=['post'])
def add_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/')

@app.route('/dojo/show/<int:id>')
def show_one_dojo(id):
    data = {
        'id':id
    }
    all_ninjas = Ninja.get_ninjas_in_dojos(data)
    one_dojo = Dojo.get_one(data)
    return render_template('dojos_show.html', all_ninjas=all_ninjas, one_dojo=one_dojo)


