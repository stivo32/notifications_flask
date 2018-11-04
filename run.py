from app import app
from sqlalchemy import create_engine
from db import db

db.init_app(app)
@app.before_first_request
def create_tables():
    from models.user import UserModel
    from models.notification import NotificationModel
    db.create_all()

app.run(debug=True, port=5000)