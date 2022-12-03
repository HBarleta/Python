from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:column>/<int:row>/<color1>/<color2>')
def checkerboard(row, column, color1, color2):
    return render_template('index.html', x=row, y=column, color1=color1, color2=color2)






if __name__ == "__main__":
    app.run(debug=True, port=5001,host="0.0.0.0")