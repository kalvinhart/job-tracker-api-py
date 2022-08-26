from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(68), nullable=False)
    company = db.Column(db.String(40), nullable=False)
    location = db.Column(db.String(40), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_applied = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    interview_date = db.Column(db.DateTime, nullable=True)
    benefits = location = db.Column(db.String(100), nullable=False)
    contact_name = db.Column(db.String(40), nullable=True)
    contact_number = db.Column(db.String(11), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    last_login = db.Column(db.DateTime, nullable=False)
    jobs = db.relationship("Job", backref=db.backref("user", lazy="joined"), lazy=True)