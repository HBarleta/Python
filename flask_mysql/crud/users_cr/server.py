from flask import Flask, redirect, render_template, request
from users_model import Users


app = Flask(__name__)
@app.route('/')
def index():
    all_users = Users.get_all()
    
    return render_template('Read(All).html', all_users=all_users)

@app.route('/users/new')
def new_user_form():
    return render_template('create.html')

@app.route('/users/create', methods=['POST'])
def create_new_user():
    Users.create(request.form)
    print(request.form)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)