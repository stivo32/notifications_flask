import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from werkzeug.contrib.fixers import ProxyFix
from resources.user import UserRegister
from resources.notification import Notification
from datetime import timedelta

app = Flask(__name__)

api = Api.app
app.wsgi_app = ProxyFix(app.wsgi_app)

api.add_resource(UserRegister, '/register')
api.add_resource(Notification, '/notification')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)