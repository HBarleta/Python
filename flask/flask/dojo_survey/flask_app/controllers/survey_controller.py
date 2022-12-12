from flask import Flask, render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.survey_model import Survey



@app.route('/')
def home():
    return render_template('index.html')

# this route will take in information from form and save it inside a session dict then redirect to info page to display form information
@app.route('/gather', methods=['POST'])
def gather():
    if Survey.validator(request.form):
        Survey.create_survey(request.form)
        return redirect('/display')
    else:
        return redirect('/')

@app.route('/display')
def display_results():
    results = Survey.get_last()
    return render_template('info.html', results=results)


# @app.route('/display')
# def display():
    #how to access form data
    #use session['form_data'] followed by ['name'], ['location'], ['fav-language'], ['comments']
    # location = session['form_data']['location']
    # name = session['form_data']['name']
    # language = session['form_data']['fav-language']
    # comments = session['form_data']['comments']
    # pass in form information as parameters used to display on page using jinja
    # return render_template('info.html', name=name, location=location, language=language, comments=comments)

@app.route('/reset')
def reset():
    #this route will clear sesssion data and redirect to root route
    session.clear()
    return redirect('/')