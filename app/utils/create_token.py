from datetime import datetime, timedelta
import jwt
import os

def create_token(user_id):
    expiry = datetime.utcnow() + timedelta(minutes=90)
    token = jwt.encode({"user_id": user_id, "exp": expiry}, os.environ.get("SECRET_KEY"))

    return token