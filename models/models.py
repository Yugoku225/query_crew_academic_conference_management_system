from . import db 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # roles like 'organizer', 'author', 'reviewer'

class Conference(db.Model):
    __tablename__ = 'conferences'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    organizer = db.relationship('User', backref='organized_conferences')

class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    abstract = db.Column(db.Text, nullable=False)
    submission_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'), nullable=False)
    author = db.relationship('User', backref='authored_papers')
    conference = db.relationship('Conference', backref='submitted_papers')

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comments = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('papers.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    end_time = db.Column(db.Time, nullable=False)
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'), nullable=True)
