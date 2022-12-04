from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/form')
def counter():
    
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def display_form():
    print(request.form)
    session['name'] = request.form['name'] #this name is what it was labeled on the form
    session['cuisine'] = request.form['cuisine']  #this name is what it was labled in the form
    return redirect('/display')
    # return render_template("display.html", name=request.form['name'], cuisine=request.form['cuisine'])
    
    
@app.route('/display')
def display_results():
    if 'name' in session:
        name = session['name']
    else:
        name = "not provided" #this session was referred in the HTML as session.cuisine jinja variable
    if not 'cuisine' in session:
        session['cuisine'] = "not provided"
    return render_template("display.html", name=name)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/form')

if __name__== "__main__":
    app.run(debug=True, port=5001)