# models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Document(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)