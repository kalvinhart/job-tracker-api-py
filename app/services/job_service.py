from flask import jsonify
from app import db
from app.models import Job, job_schema, jobs_schema
from datetime import datetime

class JobService:

    def get_all_jobs():
        jobs = Job.query.all()
        jobs_list = jobs_schema.dump(jobs)
        return jsonify(jobs_list)

    def get_job(id):
        job = Job.query.get(id)
        return job_schema.jsonify(job)

    def save_job(data):
        js_date = data.get("date")
        py_date = datetime.fromtimestamp(js_date / 1000.0)

        new_job = Job(status="Pending", title=data.get("title"), company=data.get("company"), location=data.get("location"), salary=data.get("salary"), description=data.get("description"), date_applied=py_date, benefits=data.get("benefits"), contact_name=data.get("contactName"), contact_number=data.get("contactNumber"), user_id=data.get("user_id"))
        
        db.session.add(new_job)
        db.session.commit()

        return job_schema.jsonify(new_job)