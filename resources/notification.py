from flask_restful import Resource
from flask_jwt import jwt_required
from models.notification import NotificationModel


class Notification(Resource):
    @jwt_required()
    def get(self):
        pass

    @jwt_required()
    def post(self):
        pass

    @jwt_required()
    def delete(self):
        pass


class NotificationList(Resource):
    @jwt_required()
    def get(self):
        pass
