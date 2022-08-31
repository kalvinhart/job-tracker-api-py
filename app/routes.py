from flask import request, jsonify
from app import app

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
@app.post("/users/create")
def create_user():
    user_credentials = request.get_json()

    response = UserController.create_user(user_credentials)

    match response.get_json()["status"]:
        case 201:
            return response, 201
        case 400:
            return response, 400
        case other:
            return jsonify({"status": 500, "message": "Something went wrong."}), 500

@app.post("/users/login")
def login_user():
    user_credentials = request.get_json()
    response = UserController.log_in_user(user_credentials)

    match response.get_json()["status"]:
        case 200:
            return response, 200
        case 400:
            return response, 400
        case other:
            return jsonify({"status": 500, "message": "Something went wrong."}), 500
