from crypt import methods
from flask_app import app
from flask_app.models.item import Item
from flask_app.models.dept import Dept
from flask_app.models.category import Category
from flask_app.models.whole_store import Whole_store
from flask import render_template,request,redirect,session
from flask import flash


@app.route("/inventory/cat/<int:cat_id>")
def display_category(cat_id):
    data = {"cat_id": cat_id}
    items = Category.get_totals_cat(data)
    return render_template("inventory.html", items = items) 

@app.route("/dashbord/cat/<int:cat_id>")
def get_cat_totals(cat_id):
    data = {"cat_id": cat_id}
    items = Category.get_totals_cat(data)
    return render_template("category.html", items = items) 

