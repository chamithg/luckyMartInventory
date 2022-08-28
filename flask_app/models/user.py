
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

ROLE_REGEX = re.compile(r"^[a-zA-Z]+_manager") 
FLAG_REGEX = re.compile(r"mgr_[a-zA-Z]{4}") 

class User:
    def __init__(self,data):
        self.id= data['id']
        self.user_name= data['user_name']
        self.role= data['role']
        self.flag_code= data['flag_code']
        self.pw_hash= data['pw_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #!---> reg user (login/reg)
    @classmethod
    def register_user(cls,data):
        query = "INSERT INTO users (user_name,role,flag_code,pw_hash) VALUES (%(user_name)s,%(role)s,%(flag_code)s,%(pw_hash)s);"
        return connectToMySQL('lucky_mart_schema').query_db(query,data)
    
    #!---> geting single user (login/reg)
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE user_name =%(user_name)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        users =[]
        if results:
            for user in results:
                users.append(cls(user))
                return users[0] 

    #!---> validation
    @staticmethod
    def validation(data):
        
        query = "SELECT flag_code FROM users;"
        results = connectToMySQL('lucky_mart_schema').query_db(query)
        all_flag_codes = []
        if results:
            for flag_code in results:
                all_flag_codes.append(flag_code["flag_code"])
        
        is_valid = True
        
        if len(data['user_name']) < 2:
            flash("user name must be at least 2 characters.")
            is_valid = False
        if not ROLE_REGEX.match(data['role']):
            flash("role format invalid. correct format is department_manager eg:- produce --> produce_manager ")
            is_valid = False
        if not FLAG_REGEX.match(data['flag_code']):
            flash("flag code format invalid. correct format is mgr_department(first 4 characters only) eg:- produce --> mgr_prod ")
            is_valid = False
        if data["flag_code"] in all_flag_codes:
            flash("This flag code is already in use")
            is_valid = False  
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if (data['confirm_password'])!= (data['password']) :
            flash("Passwords do not match.")
            is_valid = False
        return is_valid