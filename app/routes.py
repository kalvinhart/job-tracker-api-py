from flask import request, jsonify
from app import app
from app.models import User
from werkzeug.security import check_password_hash


from app.controllers.job_controller import JobController
from app.controllers.user_controller import UserController

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

@app.post("/users/login")
def login_user():
    user_credentials = request.get_json()
    response = UserController.log_in_user(user_credentials)

    if response != None:
        return response
    else:
        return jsonify({"message": "Incorrect username/password"}), 400
