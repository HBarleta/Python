from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models import dojo_model




@app.route('/ninja/add')
def add_ninja():
    all_dojos = dojo_model.Dojo.get_all_dojos()
    return render_template('ninja_create.html', all_dojos=all_dojos)

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    dojo_id = request.form['dojo_id']
    return redirect('/dojo/show/'+ str(dojo_id))