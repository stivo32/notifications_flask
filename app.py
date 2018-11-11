from sqlalchemy import create_engine
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from werkzeug.contrib.fixers import ProxyFix
from resources.notification import NotificationList, Notification
from resources.user import UserRegister
from datetime import timedelta

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)  # use gunicorn instead of development web-server
api = Api(app=app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # switch off flask-sqlalc_track_modif but not sqlalchemy
app.secret_key = 'somecode'

# app.wsgi_app = ProxyFix(app.wsgi_app)
jwt = JWT(app, authenticate, identity)

api.add_resource(NotificationList, '/notifications')
api.add_resource(Notification, '/notification')
api.add_resource(UserRegister, '/register')

