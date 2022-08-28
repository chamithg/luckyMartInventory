from crypt import methods
from flask_app import app
from flask_app.models.item import Item
from flask_app.models.dept import Dept
from flask_app.models.category import Category
from flask_app.models.whole_store import Whole_store
from flask import render_template,request,redirect,session
from flask import flash
import json

@app.route("/dashbord")
def whole_store_get_totals():
    totals = Whole_store.get_totals()
    data =Whole_store.get_totals_js(totals)
    meat_totals = Dept.get_totals({"dept_id":1})
    meat_totals_js = Dept.get_totals_js(meat_totals)
    produce_totals = Dept.get_totals({"dept_id":2})
    produce_totals_js = Dept.get_totals_js(produce_totals)
    dairy_totals = Dept.get_totals({"dept_id":3})
    dairy_totals_js = Dept.get_totals_js(dairy_totals)
    bakery_totals = Dept.get_totals({"dept_id":4})
    bakery_totals_js = Dept.get_totals_js(bakery_totals)
    frozen_totals = Dept.get_totals({"dept_id":5})
    frozen_totals_js = Dept.get_totals_js(frozen_totals)
    
    return render_template("dashboard.html", totals = totals, totals_js = json.dumps(data),
                        meat_totals_js = json.dumps(meat_totals_js),
                        produce_totals_js = json.dumps(produce_totals_js),
                        dairy_totals_js = json.dumps(dairy_totals_js),
                        bakery_totals_js = json.dumps(bakery_totals_js),
                        frozen_totals_js = json.dumps(frozen_totals_js)) 
