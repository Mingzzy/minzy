"""
models.py

"""
from apps import db


class Article(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    title = db.Colum(db.String(255))
    content = db.Colum(db.Text())
    category = db.Colum(db.String(255))
    data_created = db.Colum(db.DataTime(), default=db.func.now())
