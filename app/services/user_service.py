from flask import jsonify
from app import db
from app.models import User, user_schema
from werkzeug.security import check_password_hash, generate_password_hash

class UserService:

    def create_user(user_credentials):
        email, password = user_credentials.values()

        if email is None or password is None:
            return None
    
        user_exists = User.query.filter_by(email=email).first()

        if user_exists != None:
            return None
        
        pw_hash = generate_password_hash(password)
        new_user = User(email, password=pw_hash)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created"})

    def log_in_user(user_credentials):
        user = User.query.filter_by(email=user_credentials["email"]).first()

        if user != None:
            if check_password_hash(user.password, user_credentials["password"]):
                return jsonify({"email": user.email})
            
            return None
        
        return None