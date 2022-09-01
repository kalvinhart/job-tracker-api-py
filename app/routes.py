from flask import request, jsonify
from app import app

from app.controllers.job_controller import JobController
from app.controllers.user_controller import UserController
from app.middleware.token import token_required

@app.get("/")
def home():
    return "home route"

@app.get("/jobs")
@token_required
def get_all_jobs(user):
    return JobController.get_all_jobs(user["user_id"])

@app.post("/jobs/new")
@token_required
def save_job(user):
    data = request.get_json()
    return JobController.save_job(user["user_id"], data)

@app.get("/job/<string:id>")
@token_required
def get_job(user, id):
    response = JobController.get_job(user["user_id"], id)

    match response.get_json()["status"]:
        case 200:
            return response, 200
        case 403:
            return response, 403
        case 404:
            return response, 404
        case other:
            return jsonify({"status": 500, "message": "Something went wrong."}), 500

@app.put("/job/<string:id>")
@token_required
def edit_job(user, id):
    data = request.get_json()
    response = JobController.update_job(user["user_id"], id, data)

    match response.get_json()["status"]:
        case 200:
            return response, 200
        case 403:
            return response, 403
        case 404:
            return response, 404
        case other:
            return jsonify({"status": 500, "message": "Something went wrong."}), 500

@app.delete("/job/<string:id>")
@token_required
def delete_job(user, id):
    response = JobController.delete_job(user["user_id"], id)

    match response.get_json()["status"]:
        case 200:
            return response, 200
        case 403:
            return response, 403
        case 404:
            return response, 404
        case other:
            return jsonify({"status": 500, "message": "Something went wrong."}), 500

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
