#app/__init__.py 

from flask import Flask
from app.useraccounts import UserClass


# Initialize the app
app = Flask(
    __name__, instance_relative_config=True)
app.secret_key = 'dresscodesleepbehappy'

user_object = UserClass()

from app import views

# Load the config file
app.config.from_object('config')
