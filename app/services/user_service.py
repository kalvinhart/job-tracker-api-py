from flask import jsonify
from app.models import User, user_schema
from werkzeug.security import check_password_hash

class UserService:

    def create_user(user_credentials):
        pass

    def log_in_user(user_credentials):
        user = User.query.filter_by(email=user_credentials["email"]).first()

        if user != None:
            if check_password_hash(user.password, user_credentials["password"]):
                return jsonify({"email": user.email})
            else:
                return None
        else:
            return None