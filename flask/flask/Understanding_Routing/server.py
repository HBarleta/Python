from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_name(name):
    is_word = True
    for i in name:
        if i.isdigit() == True:
            is_word = False
    if is_word == True:
        return f"Hi, {name}!"
    else:
        return "Please use a name without numbers!"

@app.route('/repeat/<int:times>/<word>')
def repeat_word(word, times):
    is_word = True
    for i in word:
        if i.isdigit() == True:
            is_word = False
    if is_word == True:
        return f"<p>This is {word} multiplied {times} times</p> \n" * times
    else:
        return "Please use a name without numbers and a number to multiply with!!"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry, no response! try again!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)