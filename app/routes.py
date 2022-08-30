from flask import request, jsonify
from app import app, db
from app.models import User, Job, user_schema, job_schema
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
    return JobController.get_job(id)


@app.put("/job/<string:id>/edit")
def edit_job(id):
    return f"edit job {id}"

@app.delete("/job/<string:id>/delete")
def delete_job(id):
    return f"delete job {id}"

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
        return jsonify({"message": "Incorrect username/password"})
