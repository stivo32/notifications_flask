import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from werkzeug.contrib.fixers import ProxyFix
from resources.user import UserRegister
from resources.notification import Notification, NotificationList
from datetime import timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # switch off flask-sqlalc_track_modif but not sqlalchemy
app.secret_key = 'somecode'

api = Api(app=app)
app.wsgi_app = ProxyFix(app.wsgi_app)

jwt = JWT(app, authenticate, identity) # create /auth

api.add_resource(UserRegister, '/register')
api.add_resource(NotificationList, '/notifications')
