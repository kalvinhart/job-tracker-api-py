from flask import request, jsonify
from app import app, db
from app.models import User, Job, user_schema, job_schema
from werkzeug.security import check_password_hash
from datetime import datetime

@app.get("/")
def home():
    return "home route"

@app.get("/jobs")
def get_all_jobs():
    return "get all jobs"

@app.post("/jobs/new")
def save_job():
    data = request.get_json()
    js_date = data.get("date")
    py_date = datetime.fromtimestamp(js_date / 1000.0)
    new_job = Job(status="Pending", title=data.get("title"), company=data.get("company"), location=data.get("location"), salary=data.get("salary"), description=data.get("description"), date_applied=py_date, benefits=data.get("benefits"), contact_name=data.get("contactName"), contact_number=data.get("contactNumber"), user_id=data.get("user_id"))
    db.session.add(new_job)
    db.session.commit()
    return job_schema.jsonify(new_job)

@app.get("/job/<string:id>")
def get_job(id):
    job = Job.query.get(id)
    return job_schema.jsonify(job)


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
