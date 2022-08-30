from flask import request, jsonify
from app import app
from app.models import User
from werkzeug.security import check_password_hash


from app.controllers.job_controller import JobController

@app.get("/")
def home():
    return "home route"

@app.get("/jobs")
def get_all_jobs():
    return JobController.get_all_jobs()

@app.post("/jobs/new")
def save_job():
    data = request.get_json()
    return JobController.save_job(data)

@app.get("/job/<string:id>")
def get_job(id):
    response = JobController.get_job(id)

    if response != None:
        return response
    else:
        return jsonify({"message": f"Job not found matching id {id}"}), 404

@app.put("/job/<string:id>")
def edit_job(id):
    data = request.get_json()
    response = JobController.update_job(id, data)

    if response != None:
        return response
    else:
        return jsonify({"message": f"Job not found matching id {id}"}), 404

@app.delete("/job/<string:id>")
def delete_job(id):
    response = JobController.delete_job(id)

    if response != None:
        return response
    else:
        return jsonify({"message": f"Job not found matching id {id}"}), 404

# user

@app.get("/user/<int:id>")
def get_user(id):
    user = User.query.get(id)
    res = {"id": user.id, "email": user.email, "password": user.password}
    return jsonify(res)

@app.post("/users/login")
def login_user():
    user_credentials = request.get_json()
    user = User.query.filter_by(email=user_credentials["email"]).first()

    if check_password_hash(user.password, user_credentials["password"]):
        return jsonify({"email": user.email})
    else:
        return jsonify({"message": "Incorrect username/password"}), 400
