from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.model_user import User
from flask_app.models.model_technique import Technique
from flask_app.models import model_technique

#Display
@app.route('/techniques')
def techniques():

    data = {
        'id' : session['user']
    }

    return render_template('techniques.html', all_techniques = Technique.get_all(), user = User.get_one(data))

#Display
@app.route('/add/techniques')
def add_techniques():

    return render_template('add_tech.html')

#Action
@app.route('/add/technique', methods=['POST'])
def add_technique():
    is_valid = Technique.validate(request.form)
    if not is_valid:
        print(is_valid, 'not validating technique')
        return redirect('/add/techniques')

    data = {
        **request.form,
        'user_id' : session['user']
    }

    techniques = Technique.create(data)

    return redirect('/techniques')

#Display
@app.route('/view/technique<int:id>')
def view_technique(id):

    data = {
        'id' : id
    }

    session['tech'] = id

    return redirect('/view/tech')

@app.route('/view/tech')
def view_tech():

    data = {
        'id' : session['tech']
    }
    return render_template('view_tech.html', technique = Technique.get_one_user_from_technique(data))

#Redirect
@app.route('/edit/technique<int:id>')
def edit_technique(id):

    data = {
        'id' : id
    }

    session['tech'] = id

    return redirect('/edit/tech') 

#Display
@app.route('/edit/tech')
def edit_tech():

    data = {
        'id' : session['tech']
    }

    return render_template('edit_tech.html', technique = Technique.get_one(data))

#Action
@app.route('/edit/technique', methods=['POST'])
def update_technique():
    is_valid = Technique.validate(request.form)
    if not is_valid:
        print(is_valid, 'not validating technique')
        return redirect('/add/techniques')

    data = {
        **request.form,
        'id' : session['tech']
    }

    Technique.update(data)

    return redirect('/techniques')

#Action
@app.route('/delete/technique<int:id>')
def delete_tech(id):
    data = {
        'id': id
    }

    print('************************************')
    Technique.delete(data)
    print('technique deleted')
    return redirect('/techniques')

#Action
@app.route('/search', methods=['POST'])
def search_techniques():

    data = {
        'name' : request.form['search']
    }
    tech_in_db = Technique.get_one_tech_search(data)

    if not tech_in_db:
        flash('Technique does not exist', 'err_tech_search')
        return redirect('/techniques')

    tech = tech_in_db.id
    session['tech'] = tech
    return redirect('/view/tech')