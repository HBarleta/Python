from flask import Flask, render_template

app = Flask(__name__)
@app.route('/play/')
def three_boxes():
    return render_template("three_boxes.html")

@app.route('/play/<int:x>')
def multi_box(x):
    return render_template("multi_boxes.html", x=x)

@app.route('/play/<int:x>/<color>')
def multi_color_box(x, color):
    return render_template("color_choice.html", x=x, color=color)

if __name__ == "__main__":
    app.run(debug=True, port=5001,host="0.0.0.0")