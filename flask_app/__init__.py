from flask import Flask

from flask_app.models.user import User
from flask_app.models.item import Item
from flask_app.models.dept import Dept
from flask_app.models.category import Category
from flask_app.models.whole_store import Whole_store

app = Flask(__name__)
app.secret_key = "Benny Bob wuz heer."