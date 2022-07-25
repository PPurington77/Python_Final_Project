from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_technique import Technique

#Display
@app.route('/techniques')
def techniques():

    return render_template('techniques.html', all_techniques = Technique.get_all())

#Display
@app.route('/add/techniques')
def add_techniques():

    return render_template('add_tech.html')