from crypt import methods
from unicodedata import category
from flask_app import app
from flask_app.models.all_cat import All_cat
from flask_app.models.all_dept import All_dept
from flask_app.models.item import Item
from flask_app.models.dept import Dept
from flask_app.models.category import Category
from flask import render_template,request,redirect,session
from flask import flash
import json



@app.route("/departments")
def display_depts():
    
    meat_totals_js = Dept.get_totals_js(Dept.get_totals({"dept_id":1})) 
    produce_totals_js = Dept.get_totals_js(Dept.get_totals({"dept_id":2}))    
    dairy_totals_js = Dept.get_totals_js(Dept.get_totals({"dept_id":3}))   
    bakery_totals_js = Dept.get_totals_js(Dept.get_totals({"dept_id":4}))  
    frozen_totals_js = Dept.get_totals_js(Dept.get_totals({"dept_id":5}))
    
    meat_totals = Dept.get_totals({"dept_id":1})
    produce_totals = Dept.get_totals({"dept_id":2})
    dairy_totals = Dept.get_totals({"dept_id":3})
    bakery_totals = Dept.get_totals({"dept_id":4})
    frozen_totals = Dept.get_totals({"dept_id":5})
    
    
    return render_template("departments.html", meat_totals = meat_totals,
                        produce_totals = produce_totals,
                        dairy_totals = dairy_totals,
                        bakery_totals = bakery_totals,
                        frozen_totals = frozen_totals,
                        meat_totals_js = json.dumps(meat_totals_js),
                        produce_totals_js = json.dumps(produce_totals_js),
                        dairy_totals_js = json.dumps(dairy_totals_js),
                        bakery_totals_js = json.dumps(bakery_totals_js),
                        frozen_totals_js = json.dumps(frozen_totals_js)) 

@app.route("/department/<int:dept_id>")
def display_single_dept(dept_id):
    dept_total = Dept.get_totals({"dept_id":dept_id})
    dept_total_js = Dept.get_totals_js(Dept.get_totals({"dept_id":dept_id}))
    dept_data = All_dept.one_dept({"dept_id":dept_id})
    cats_data = All_cat.all_cats({"dept_id":dept_id})
    cats =[]
    cats_js = []
    
    for i in range(len(cats_data)):
        single_cat = Category.get_totals({"cat_id":cats_data[i].id })
        cats.append(single_cat)
        single_cat_js = Category.get_totals_js(Category.get_totals({"cat_id":cats_data[i].id }))
        cats_js.append(json.dumps(single_cat_js))
    return render_template("dept.html", dept_total = dept_total, dept_total_js = json.dumps(dept_total_js),dept_data =dept_data,cats_data = cats_data, cats=cats, cats_js =cats_js, dept_id = dept_id)
    
@app.route("/view_item/<int:id>")
def display_single_item(id):
    item_total = Dept.get_totals_single({"id":id})
    item_total_js = Dept.get_totals_js( Dept.get_totals_single({"id":id}))
    item = Item.get_single_item({"id":id})
    print(item_total_js)
    
    return render_template("item.html", item_total = item_total, item_total_js = json.dumps(item_total_js), item = item)
