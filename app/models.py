from datetime import datetime
from app import db, ma
from sqlalchemy.sql import func

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(68), nullable=False)
    company = db.Column(db.String(40), nullable=False)
    location = db.Column(db.String(40), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_applied = db.Column(db.DateTime(timezone=True), index=True, nullable=False, server_default=func.now())
    date_updated = db.Column(db.DateTime(timezone=True), server_default=func.now())
    interview_date = db.Column(db.DateTime(timezone=True), index=True, nullable=True)
    benefits = db.Column(db.String(100), nullable=False)
    contact_name = db.Column(db.String(40), nullable=True)
    contact_number = db.Column(db.String(11), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, status, title, company, location, salary, description, date_applied, benefits, contact_name, contact_number, user_id):
        self.status = status
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.description = description
        self.date_applied = date_applied
        self.benefits = benefits
        self.contact_name = contact_name
        self.contact_number = contact_number
        self.user_id = user_id

class JobSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Job

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_login = db.Column(db.DateTime(timezone=True), server_default=func.now())
    jobs = db.relationship("Job", backref=db.backref("user", lazy="joined"), lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

user_schema = UserSchema()