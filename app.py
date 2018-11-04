from sqlalchemy import create_engine
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from werkzeug.contrib.fixers import ProxyFix
from resources.notification import Notification
from datetime import timedelta

app = Flask(__name__)

api = Api(app=app)
app.wsgi_app = ProxyFix(app.wsgi_app)
api.add_resource(Notification, '/notification')
