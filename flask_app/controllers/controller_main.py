from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
# from flask_app.models.model_user import User
# from flask_app.models.model_show import Show



#Display
@app.route('/')
def home():

    return render_template('home.html')

