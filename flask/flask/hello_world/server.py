from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/new_route')
def hi_there_again():
    return "Hey a different route!"


@app.route('/hello<name>/<int:times>')
def hi_name(name, times):
    return f"<p>Hello, {name}\n</p>" * times

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")