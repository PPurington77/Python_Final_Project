from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_technique import Technique
from flask_app.models import model_user

#Display
@app.route('/login')
def login_and_register():

        
    if 'user' not in session:
        return render_template('/login.html')

    data = {
        'id' : session['user']
    }

    return redirect('/dashboard')

#Action
@app.route('/register', methods=['POST'])
def register():
    is_valid = User.validate(request.form)
    if not is_valid:
        print('registration not valid')
        return redirect('/login')

    hash_pw = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        'password' : hash_pw
    }

    user = User.create(data)
    print(user)
    session['user'] = user
    print(user)

    return redirect('/dashboard')

#Action
@app.route('/login_user', methods=['POST'])
def login_user():

    data = {'email' : request.form['email']}
    user_in_db = User.get_one_login(data)

    if not user_in_db:
        flash('Invalid Email', 'err_login_email')
        return redirect('/login')

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Password', 'err_login_password')
        return redirect('/login')

    print('email and password are valid')
    user = user_in_db
    session['user'] = user.id 

    return redirect('/dashboard')

#Display
@app.route('/dashboard')
def dashboard():
    
    if 'user' not in session:
        return redirect ('/login')

    data = {
        'id' : session['user']
    }

    return render_template('dashboard.html', user = User.get_one(data))

#Action
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')

#Diplay
@app.route('/go/update')
def go_update():
    data = {
        'id' : session['user']
    }

    return render_template('update.html', user = User.get_one(data))

#Action
@app.route('/update', methods=['POST'])
def update():

    is_valid = User.validate_update(request.form)
    if not is_valid:
        print('update not valid')
        return redirect('/go/update')

    data = {
        **request.form,
        'id' : session['user']
    }

    User.update(data)

    return redirect('/dashboard')

#Action
@app.route('/delete')
def delete():
    data = {
        'id': session['user']
    }

    print('************************************')
    print(data)
    User.delete(data)
    print('user deleted')
    session.clear()
    return redirect('/login')