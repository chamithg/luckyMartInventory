from flask import Flask
from flask_app.controllers import users
from flask_app.controllers import items
from flask_app.controllers import depts
from flask_app.controllers import whole_stores
from flask_app.controllers import categories
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)

