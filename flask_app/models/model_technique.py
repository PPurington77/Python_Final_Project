from flask_app.config.mysqlconnection import connectToMySQL 
import re
from flask import flash
from flask_app import bcrypt
from flask_app.models import model_user

# DATABASE = 'keystonemma_db'
DATABASE = 'xteh85kabs9aiddo'  

class Technique:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.instructions = data['instructions']
        self.type = data['type']
        self.belt_level = data['belt_level']
        self.link = data['link']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.owner = {}



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM techniques JOIN users ON users.id = techniques.user_id"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        if results:
            all_techniques = []
            for dict in results:
                technique = cls(dict)
                user_data = {
                    'id':dict['users.id'],
                    'first_name':dict['first_name'],
                    'last_name':dict['last_name'],
                    'email':dict['email'],
                    'px':dict['px'],
                    'password':dict['password'],
                    'created_at':dict['users.created_at'],
                    'updated_at':dict['users.updated_at']
                }
                user = model_user.User(user_data)
                technique.owner = user
                all_techniques.append(technique)
            return all_techniques
        return []

    @classmethod
    def get_one_user_from_technique(cls, data):
        query = "SELECT * FROM techniques JOIN users ON users.id = techniques.user_id WHERE techniques.id = %(id)s"

        results = connectToMySQL(DATABASE).query_db(query, data)
        technique = cls(results[0])

        user_data = {
            'id':results[0]['users.id'],
            'first_name':results[0]['first_name'],
            'last_name':results[0]['last_name'],
            'email':results[0]['email'],
            'px':results[0]['px'],
            'password':results[0]['password'],
            'created_at':results[0]['users.created_at'],
            'updated_at':results[0]['users.updated_at']
        }
        owner = model_user.User(user_data)
        technique.owner = owner
        return technique

    @classmethod
    def create(cls, data):
        query = "INSERT INTO techniques (name, instructions, type, belt_level, link, user_id, created_at, updated_at) VALUES (%(name)s, %(instructions)s, %(type)s, %(belt_level)s, %(link)s, %(user_id)s, NOW(), NOW());"
        
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM techniques WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            technique = cls(result[0])
            return technique
        return False

    @classmethod
    def get_one_tech_search(cls, data):
        query = "SELECT * FROM techniques WHERE name = %(name)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        if result:
            technique = cls(result[0])
            return technique
        print('technique doesnt exist')
        print('----------------------------------------')

        return False


    @classmethod
    def update(cls, data):
        query = "UPDATE techniques SET name = %(name)s, instructions = %(instructions)s, type = %(type)s, belt_level = %(belt_level)s, link = %(link)s, updated_at = Now() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM techniques WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['name']) < 2:
            flash('Enter Name', 'err_name')
            print('name')
            is_valid = False

        if len(data['instructions']) < 2:
            flash('Enter Instructions', 'err_instructions')
            print('instructions')
            is_valid = False

        if len(data['type']) < 2:
            print('type')
            flash('Enter move type', 'err_type')
            is_valid = False


        if not data['belt_level']:
            flash('Choose belt level', 'err_belt_level')
            print('belt_level')
            is_valid = False

        print(is_valid)
        return is_valid



