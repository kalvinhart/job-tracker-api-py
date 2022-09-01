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

    valid_response_codes = [200, 403, 404]
    response_status = response.get_json()["status"]

    if response_status not in valid_response_codes:
        return jsonify({"status": 500, "message": "Something went wrong."}), 500

    return response, response_status

@app.put("/job/<string:id>")
@token_required
def edit_job(user, id):
    data = request.get_json()
    response = JobController.update_job(user["user_id"], id, data)

    valid_response_codes = [200, 403, 404]
    response_status = response.get_json()["status"]

    if response_status not in valid_response_codes:
        return jsonify({"status": 500, "message": "Something went wrong."}), 500

    return response, response_status

@app.delete("/job/<string:id>")
@token_required
def delete_job(user, id):
    response = JobController.delete_job(user["user_id"], id)

    valid_response_codes = [200, 403, 404]
    response_status = response.get_json()["status"]

    if response_status not in valid_response_codes:
        return jsonify({"status": 500, "message": "Something went wrong."}), 500

    return response, response_status

# user
@app.post("/users/create")
def create_user():
    user_credentials = request.get_json()

    response = UserController.create_user(user_credentials)

    valid_response_codes = [201, 400]
    response_status = response.get_json()["status"]

    if response_status not in valid_response_codes:
        return jsonify({"status": 500, "message": "Something went wrong."}), 500

    return response, response_status

@app.post("/users/login")
def login_user():
    user_credentials = request.get_json()
    response = UserController.log_in_user(user_credentials)

    valid_response_codes = [200, 400]
    response_status = response.get_json()["status"]

    if response_status not in valid_response_codes:
        return jsonify({"status": 500, "message": "Something went wrong."}), 500

    return response, response_status
