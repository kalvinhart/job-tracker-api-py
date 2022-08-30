from datetime import datetime
from flask import jsonify
from app import db
from app.models import Job, job_schema, jobs_schema
from app.utils.date import convert_to_datetime

class JobService:

    def get_all_jobs():
        jobs = Job.query.all()
        jobs_list = jobs_schema.dump(jobs)
        return jsonify(jobs_list)

    def get_job(id):
        job = Job.query.get(id)
        return job_schema.jsonify(job)

    def save_job(data):
        py_date = convert_to_datetime(data.get("date"))

        new_job = Job(status="Pending", title=data.get("title"), company=data.get("company"), location=data.get("location"), salary=data.get("salary"), description=data.get("description"), date_applied=py_date, benefits=data.get("benefits"), contact_name=data.get("contactName"), contact_number=data.get("contactNumber"), user_id=data.get("user_id"))
        
        db.session.add(new_job)
        db.session.commit()

        return job_schema.jsonify(new_job)

    def update_job(id, data):
        job = Job.query.get(id)

        if job != None:
            py_date_applied = convert_to_datetime(data.get("date"))

            if data.get("interview") != None:
                py_date_interview = convert_to_datetime(data.get("interview"))
                job.interview_date = py_date_interview

            job.date_applied = py_date_applied
            job.status = data.get("status")
            job.title = data.get("title")
            job.company = data.get("company")
            job.location = data.get("location")
            job.salary = data.get("salary")
            job.description = data.get("description")
            job.benefits = data.get("benefits")
            job.contact_name = data.get("contactName")
            job.contact_number = data.get("contactNnumber")
            job.date_updated = datetime.utcnow()

            db.session.commit()

            return job_schema.jsonify(job)
        
        else:
            return None