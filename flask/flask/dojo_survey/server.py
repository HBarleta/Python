from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "There are no secrets in the dojo"

#root route
@app.route('/')
def home():
    return render_template('index.html')

# this route will take in information from form and save it inside a session dict then redirect to info page to display form information
@app.route('/gather', methods=['POST'])
def gather():
    session['form_data'] = request.form
    return redirect('/display')

@app.route('/display')
def display():
    #how to access form data
    #use session['form_data'] followed by ['name'], ['location'], ['fav-language'], ['comments']
    location = session['form_data']['location']
    name = session['form_data']['name']
    language = session['form_data']['fav-language']
    comments = session['form_data']['comments']
    # pass in form information as parameters used to display on page using jinja
    return render_template('info.html', name=name, location=location, language=language, comments=comments)

@app.route('/reset')
def reset():
    #this route will clear sesssion data and redirect to root route
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True, port=5001)
    
    