from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secrets are for losers"


@app.route('/')
def home():
    counter = 0
    if 'click' in session:
        counter += 1
        print('counter')
    return render_template("index.html", counter=counter)

@app.route('/count', methods = ['POST'])
def counter():
    session['click'] = request.form
    print(session)
    return redirect('/')

@app.route('/destroy_cookies')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)