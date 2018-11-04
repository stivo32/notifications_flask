from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.notification import NotificationModel
from datetime import datetime


class Notification(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'message', type=str, required=True, help='This field cannot be blank'
    )

    @jwt_required()
    def get(self):
        pass

    @jwt_required()
    def post(self):
        data = Notification.parser.parse_args()
        if NotificationModel.find_by_message_and_user_id(data['message'], current_identity.id):
            return {'message': 'Notification with such message already exists'}, 400
        temp_datetime = datetime.now()
        notification = NotificationModel(data['message'], current_identity.id, temp_datetime)
        try:
            notification.save_to_db()
        except:
            return {"message": "Error occured while inserting item"}, 500
        return notification.jsonify(), 201

    @jwt_required()
    def delete(self):
        pass


class NotificationList(Resource):
    @jwt_required()
    def get(self):
        return {
            "notifications": [
                notification.jsonify()
                for notification
                in NotificationModel.query.filter_by(user_id=current_identity.id).all()
            ]
        }, 200
