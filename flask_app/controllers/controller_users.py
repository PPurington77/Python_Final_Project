# from flask_app import app, bcrypt
# from flask import render_template, redirect, request, session, flash
# # from flask_app.models.model_user import User
# # from flask_app.models.model_show import Show  #update these please



# #Display
# @app.route('/')
# def login_and_register():
#     if 'user' in session:
#         user = session['user']
#         return redirect(f'/dashboard/{user}') #automatically goes to dashboard page if user is logged in and in session
#     return render_template('login.html')

# #Action
# @app.route('/register', methods=["POST"])
# def register():
#     is_valid = User.validate(request.form)
#     if not is_valid:
#         print(is_valid)
#         return redirect('/')

#     hash_pw = bcrypt.generate_password_hash(request.form['password'])

#     data = {
#         **request.form, 
#         'password' : hash_pw
#     }

#     user = User.create(data)
#     session['user'] = user.id
#     print(user)

#     return redirect('/dashboard/')

# #Display
# @app.route('/dashboard/')
# def dashboard():


#     if 'user' not in session:
#         return redirect ('/')

#     data = {
#         'id' : session['user']
#     }
#                                             #imports the user to thepage....imports all of your other class also
#     return render_template('dashboard.html', user = User.get_one(data), all_shows = Show.get_all())
#                                                                         #make sure to update this
# @app.route('/login', methods=["POST"])
# def login():
    
#     data = { 'email' : request.form['email']}
#     user_in_db = User.get_one_login(data)

#     if not user_in_db:
#         flash('Invalid Email', 'err_login_email')
#         return redirect ('/')

#     if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
#         flash('Invalid Password', 'err_login_password')
#         return redirect('/')

#     print('email and password are valid')
#     user = user_in_db
#     session['user'] = user.id
#     user = session['user']

#     return redirect ('/dashboard/')

# # #Action
# @app.route('/logout', methods=['GET'])
# def logout():

#     session.clear()

#     return redirect('/')