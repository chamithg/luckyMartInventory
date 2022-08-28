from crypt import methods
from dataclasses import dataclass
from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.item import Item
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route("/")
def index():
    return render_template("login.html")

#!register method
@app.route("/register", methods =["POST"])
def register():
    if not User.validation(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "flag_code": request.form["flag_code"],
        "user_name": request.form["user_name"],
        "role": request.form["role"],
        "pw_hash": pw_hash,
    }    
    User.register_user(data)
    logged_user = User.get_one_user(data)
    session['role'] = logged_user.role
    session['user_name'] = logged_user.user_name
    session['flag_code'] = logged_user.flag_code
    session['pw_hash'] = logged_user.pw_hash
    session['id'] = logged_user.id
    
    return redirect("/dashboard")


#!login method
@app.route("/login", methods =["POST"])
def login():
    data ={"user_name" :request.form['user_name']}
    logged_user = User.get_one_user(data)
    if not logged_user:
        flash("Invalid User Name/Password")
        return redirect("/")
    if bcrypt.check_password_hash(logged_user.pw_hash, request.form["password"]):
        session['role'] = logged_user.role
        session['user_name'] = logged_user.user_name
        session['flag_code'] = logged_user.flag_code
        session['pw_hash'] = logged_user.pw_hash
        session['id'] = logged_user.id
    else:
        flash("Wrong Password.")
        return redirect("/")
    return redirect("/dashboard")

#!dashboard display method   
@app.route("/dashboard")
def dashboard():
    if 'id' not in session:
        flash("No any logged in users")
        return redirect('/')
    return redirect("/dashbord")

#!logout method
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

