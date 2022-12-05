from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secrets are for losers"
visits = 0
# global variable is accessible inside this entire program

@app.route('/')
def home():
    # global variable used to keep track of page visits
    global visits
    # this conditional will check if a session['click'] is inside session dict. This means a click was already performed on button
    if 'click' in session:
        visits += 1
    # count = visits in order to link this global variable to the HTML jinja variable
    count = visits 
    return render_template("index.html", count = count )

@app.route('/count', methods = ['POST'])
def counter():    
    session['click'] = request.form
    # request.form store in a session cookie to keep track of IF the click button was clicked
    print(session['click'])
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    global visits
    visits = 0
    session.clear()
    # sets visits back to 0 and clears session dict then redirects back to root
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)