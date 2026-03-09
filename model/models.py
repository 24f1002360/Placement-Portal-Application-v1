from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db= SQLAlchemy()

class Admin(db.Model):
    __tablename__="admin" 
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50), nullable=False, unique=True)
    email=db.Column(db.String(100))
    password=db.Column(db.String(200), nullable=False)
    
class Student(db.Model):
    __tablename__="students"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(200), nullable=False)
    department=db.Column(db.String(100))
    skills=db.Column(db.String(200))
    resume=db.Column(db.String(200))
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    applications=db.relationship('Application', backref='student')
    
class Company(db.Model):
    __tablename__="companies"
    id=db.Column(db.Integer, primary_key=True)
    company_name=db.Column(db.String(120), nullable=False)
    email=db.Column(db.String(120), nullable=False, unique=True)
    password=db.Column(db.String(200), nullable=False)
    hr_contact=db.Column(db.String(100))
    website=db.Column(db.String(200))
    approval_status=db.Column(db.String(50), default="pending")
    drives=db.relationship('Drive', backref='company')
    
class Drive(db.Model):
    __tablename__="drives"
    id=db.Column(db.Integer, primary_key=True)
    company_id=db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    job_title=db.Column(db.String(120), nullable=False)
    job_description=db.Column(db.Text)
    eligibility =db.Column(db.String(200))
    location=db.Column(db.String(100))
    salary=db.Column(db.Integer)
    deadline=db.Column(db.DateTime)
    status =db.Column(db.String(50), default="active")
    applications=db.relationship('Application', backref='drive')
    
class Application(db.Model):
    __tablename__="applications"
    id=db.Column(db.Integer, primary_key=True)
    student_id=db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    drive_id=db.Column(db.Integer, db.ForeignKey('drives.id'), nullable=False)
    status=db.Column(db.String(50), default="applied")
    application_date=db.Column(db.DateTime, default=datetime.utcnow)        
        