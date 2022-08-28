from flask_app.config.mysqlconnection import connectToMySQL


class All_dept:
    def __init__(self,data):
        self.id= data['id']
        self.dept_name= data['dept_name']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        
    @classmethod
    def all_depts(cls):
        query = "SELECT * FROM  departments;"
        results = connectToMySQL('lucky_mart_schema').query_db(query)
        depts =[]
        if results:
            for dept in results:
                depts.append(cls(dept))   
        return depts
    
    @classmethod
    def one_dept(cls,data):
        query = "SELECT * FROM  departments WHERE id = %(dept_id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        depts =[]
        print(results)
        if results:
            for dept in results:
                depts.append(cls(dept))   
        return depts[0]
        