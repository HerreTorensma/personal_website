from datetime import datetime
from app import db

class ImageTag(db.Model):
    __tablename__ = "image_tag"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(50), unique=True, nullable=False)

class Image(db.Model):
    __tablename__ = "image"
    id = db.Column("id", db.Integer, primary_key=True)
    date_added = db.Column("date_added", db.DateTime, default=datetime.now())
    file_name = db.Column("file_name", db.String(100), unique=True, nullable=False)
    tags = db.relationship("tag", secondary="")