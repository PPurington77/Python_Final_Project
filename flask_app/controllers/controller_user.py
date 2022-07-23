from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User

#Display
@app.route('/login')
def login_and_register():

        
    if 'user' not in session:
        return render_template('/login.html')

    data = {
        'id' : session['user']
    }

    return render_template('dashboard.html', user = User.get_one(data))

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
    session['user'] = user.id 
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
        return redirect ('/')

    data = {
        'id' : session['user']
    }

    return render_template('dashboard.html', user = User.get_one(data))

#Action
@app.route('/logout')
def logout():

    session.clear()

    return redirect('/')