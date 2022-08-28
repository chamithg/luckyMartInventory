from flask_app.config.mysqlconnection import connectToMySQL



class All_cat:
    def __init__(self,data):
        self.id= data['id']
        self.cat_name= data['cat_name']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        
    @classmethod
    def all_cats(cls,data):
        query = "SELECT * FROM  categories WHERE dept_id  = %(dept_id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        cats =[]
        for cat in results:
            cats.append(cls(cat))
        
        return cats
        
    @classmethod
    def one_cat(cls,data):
        query = "SELECT * FROM  categories WHERE id  = %(cat_id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        cats =[]
        if results:
            for cat in results:
                cats.append(cls(cat))
        
        return cats[0]
        
        