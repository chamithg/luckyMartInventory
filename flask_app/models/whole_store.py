from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.item import Item
from flask import flash
import re


class Whole_store:
    def __init__(self,data):
        self.total_prev_sales = data["total_prev_sales"]
        self.total_prev_sales_target = data["total_prev_sales_target"]
        self.total_prev_cost = data["total_prev_cost"]
        self.total_prev_income =  data["total_prev_sales"] - data["total_prev_cost"]
        self.total_prev_shrink =  data["total_prev_shrink"]
        self.total_prev_shrink_target =  data["total_prev_shrink_target"]
        self.total_nxt_sales_proj = data["total_nxt_sales_proj"]
        self.total_nxt_sales_target = data["total_nxt_sales_target"]
        self.total_nxt_cost_proj = data["total_nxt_cost_proj"]
        self.total_nxt_income_proj = data["total_nxt_sales_proj"]-data["total_nxt_cost_proj"]
        self.total_nxt_shrink_proj = data["total_nxt_shrink_proj"]
        self.total_nxt_shrink_target = data["total_nxt_shrink_target"]
        self.sales_stock_in_hand = data["sales_stock_in_hand"]
        self.cost_stock_in_hand = data["cost_stock_in_hand"]
        
        
        
    @classmethod
    def get_totals(cls):
        query = "SELECT sum(unit_price_old * item_count ) as sales_stock_in_hand, sum(cost_old * item_count ) as cost_stock_in_hand, sum(prev_week_sale * unit_price_old) as total_prev_sales,sum(prev_week_target*unit_price_new) as total_prev_sales_target, sum(prev_week_sale* cost_old) as total_prev_cost,sum(prev_week_shrink * unit_price_old) as total_prev_shrink,sum(prev_week_shrink_target* unit_price_old)as total_prev_shrink_target,sum(nxt_week_sale_proj * unit_price_new)as total_nxt_sales_proj,sum(nxt_week_target * unit_price_new)as total_nxt_sales_target,sum(nxt_week_sale_proj * cost_old)as total_nxt_cost_proj,sum(nxt_week_shrink_proj * unit_price_new)as total_nxt_shrink_proj,sum(nxt_week_shrink_target * unit_price_new)as total_nxt_shrink_target FROM  inventory LEFT JOIN sales ON sales.inv_id = inventory.id LEFT JOIN categories ON categories.id = inventory.cat_id LEFT JOIN  departments ON departments.id = categories.dept_id;"
        results = connectToMySQL('lucky_mart_schema').query_db(query)
        items =[]
        if results:
            for dept in results:
                items.append(cls(dept))   
        print(items)
        return items[0]

    
    def get_totals_js(totals):
        data ={  
        "total_prev_sales":totals.total_prev_sales,
        "total_prev_sales_target":totals.total_prev_sales_target,
        "total_prev_cost":totals.total_prev_cost,
        "total_prev_income":totals.total_prev_income,
        "total_prev_shrink":totals.total_prev_shrink,
        "total_prev_shrink_target":totals.total_prev_shrink_target,
        "total_nxt_sales_proj":totals.total_nxt_sales_proj,
        "total_nxt_sales_target":totals.total_nxt_sales_target,
        "total_nxt_cost_proj":totals.total_nxt_cost_proj,
        "total_nxt_income_proj":totals.total_nxt_income_proj,
        "total_nxt_shrink_proj":totals.total_nxt_shrink_proj,
        "total_nxt_shrink_target":totals.total_nxt_shrink_target,
        "sales_stock_in_hand":totals.sales_stock_in_hand,
        "cost_stock_in_hand":totals.cost_stock_in_hand,
        }
        
        
        return data