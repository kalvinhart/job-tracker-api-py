from flask import jsonify
from app import db
from app.models import User
from werkzeug.security import check_password_hash, generate_password_hash

from app.utils.create_token import create_token

class UserService:

    def create_user(user_credentials):
        email, password = user_credentials.values()

        if email is None or password is None:
            return jsonify({"status": 400, "message": "Email and Password are required fields."})
    
        user_exists = User.query.filter_by(email=email).first()

        if user_exists != None:
            return jsonify({"status": 400, "message": "User already exists."})
        
        pw_hash = generate_password_hash(password)
        new_user = User(email, password=pw_hash)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"status": 201, "message": "User created"})

    def log_in_user(user_credentials):
        email, password = user_credentials.values()

        user = User.query.filter_by(email=email).first()

        if user != None:
            if check_password_hash(user.password, password):
                token = create_token(user.id)
                return jsonify({"status": 200, "message": "User logged in.", "email": user.email, "token": f"Bearer {token}"})
            
            return jsonify({"status": 400, "message": "Username/password incorrect."})
        
        return jsonify({"status": 400, "message": "Username/password incorrect."})