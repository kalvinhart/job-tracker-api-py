from flask import request, jsonify
from functools import wraps
from app.models import User
import jwt
import os

def token_required(func):

    @wraps(func)
    def decorator(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"]

        if not token:
            return jsonify({"status": 401, "message": "Invalid token."}), 401

        token_code = token.split(" ")[1]
        
        try:
            token_data = jwt.decode(token_code, os.environ.get("SECRET_KEY"), algorithms="HS256")
            user = User.query.get(token_data["user_id"])
        except:
            return jsonify({"status": 401, "message": "Invalid token."}), 401

        return func({"user_id": user.id, "email": user.email}, *args, **kwargs)

    return decorator