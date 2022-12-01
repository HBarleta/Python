from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/new_route')
def new_route():
    return "Hey look a different route"


if __name__ == "__main__":
    app.run(debug=True,port=5001)