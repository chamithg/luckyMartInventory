from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Item:
    def __init__(self,data):
        self.id= data['id']
        self.item_desc= data['item_desc']
        self.item_count= data['item_count']
        self.cost_old= data['cost_old']
        self.unit_price_old= data['unit_price_old']
        self.unit_price_new= data['unit_price_new']
        self.flag_by= data['flag_by']
        self.status= data['status']
        self.cat_id= data['cat_id']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
        self.prev_week_sale= data["prev_week_sale"]
        self.prev_week_target= data["prev_week_target"]
        self.prev_week_shrink= data["prev_week_shrink"]
        self.prev_week_shrink_target= data["prev_week_shrink_target"]
        self.nxt_week_sale_proj= data["nxt_week_sale_proj"]
        self.nxt_week_target= data["nxt_week_target"]
        self.nxt_week_shrink_proj= data["nxt_week_shrink_proj"]
        self.nxt_week_shrink_target= data["nxt_week_shrink_target"]
        self.cat_id = data["cat_id"]
        self.cat_name = data["cat_name"]
        self.dept_id = data["dept_id"]
        self.dept_name = data["dept_name"]
        self.sales_plan = data["sales_plan"]
        
        
        
        
        
    # @classmethod
    # def new_msg_rec(cls,data):
    #     query = "INSERT INTO rec_msgs(rec_msg, user_id, sender) VALUES (%(sent_msg)s,%(receiver_id)s,%(sender)s);"
    #     results = connectToMySQL('wall_schema').query_db(query,data)
    #     return results
    
    
    @classmethod
    def get_all_items(cls):
        query = "SELECT * FROM  inventory LEFT JOIN sales ON sales.inv_id = inventory.id LEFT JOIN  categories ON categories.id = inventory.cat_id LEFT JOIN  departments ON departments.id = categories.dept_id;"
        results = connectToMySQL('lucky_mart_schema').query_db(query)
        items =[]
        if results:
            for item in results:
                items.append(cls(item))
    
        return items
    
    @classmethod
    def get_marked_items(cls):
        query = "SELECT * FROM  inventory LEFT JOIN sales ON sales.inv_id = inventory.id LEFT JOIN  categories ON categories.id = inventory.cat_id LEFT JOIN  departments ON departments.id = categories.dept_id WHERE flag_by IS NOT NULL;"
        results = connectToMySQL('lucky_mart_schema').query_db(query)
        items =[]
        if results:
            for item in results:
                items.append(cls(item))
    
        return items
            
    
    @classmethod
    def get_single_item(cls,data):
        query = "SELECT * FROM  inventory LEFT JOIN sales ON sales.inv_id = inventory.id LEFT JOIN  categories ON categories.id = inventory.cat_id LEFT JOIN  departments ON departments.id = categories.dept_id WHERE inventory.id = %(id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        items =[]
        if results:
            for item in results:
                items.append(cls(item))
                return items[0]
    
    @classmethod
    def get_all_items_dept(cls,data):
        query = "SELECT * FROM  inventory LEFT JOIN sales ON sales.inv_id = inventory.id LEFT JOIN  categories ON categories.id = inventory.cat_id LEFT JOIN  departments ON departments.id = categories.dept_id WHERE dept_id = %(dept_id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        items =[]
        if results:
            for item in results:
                items.append(cls(item))
    
        return items
    
    @classmethod
    def get_all_items_cat(cls,data):
        query = "SELECT * FROM  inventory LEFT JOIN sales ON sales.inv_id = inventory.id LEFT JOIN  categories ON categories.id = inventory.cat_id LEFT JOIN  departments ON departments.id = categories.dept_id WHERE cat_id = %(cat_id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        items =[]
        if results:
            for item in results:
                items.append(cls(item))
    
        return items        
            

            
    @classmethod
    def edit_sales(cls,data):
        query = "UPDATE inventory LEFT JOIN sales ON sales.inv_id = inventory.id SET unit_price_new = %(unit_price_new)s,nxt_week_sale_proj = %(nxt_week_sale_proj)s,nxt_week_shrink_proj = %(nxt_week_shrink_proj)s, sales_plan =%(sales_plan)s, status = 'active'  WHERE inventory.id = %(id)s;"
        results = connectToMySQL('lucky_mart_schema').query_db(query,data)
        return results
    
    
    @classmethod
    def mark_item(cls,data):
        query = "UPDATE inventory SET flag_by = %(flag_code)s WHERE id = %(id)s;"
        return connectToMySQL('lucky_mart_schema').query_db(query,data)
        
    
    @classmethod
    def unmark_item(cls,data):
        query = "UPDATE inventory SET flag_by = NULL WHERE id = %(id)s;"
        return connectToMySQL('lucky_mart_schema').query_db(query,data)
        
    @classmethod
    def change_status(cls,data):
        query = "UPDATE inventory SET status = %(status)s WHERE id = %(id)s;"
        return connectToMySQL('lucky_mart_schema').query_db(query,data)
        
    
