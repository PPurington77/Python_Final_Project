from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_technique import Technique



#Display
@app.route('/')
def home():

    return render_template('home.html')

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/classes')
def classes():

    return render_template('classes.html')

@app.route('/contact')
def contact():

    return render_template('contact.html')