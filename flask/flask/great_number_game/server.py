from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "There are no secrets in the dojo"
try_counter = 0
correct_guess = random.randint(1,100)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess_display')
def display():
    global correct_guess
    global try_counter
    attempts = try_counter
    answer = correct_guess
    test_guess = int(session['guess']['guess'])
    return render_template('guess.html', guess=test_guess, answer=answer, attempts=attempts)

@app.route('/guess', methods=['POST'])
def guess():
    global try_counter
    try_counter += 1
    session['guess'] = request.form
    print(correct_guess)
    return redirect('/guess_display')

@app.route('/reset')
def reset():
    global correct_guess
    correct_guess = random.randint(1,100)
    print(correct_guess)
    try_counter = 0
    session.clear()
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")