# здесь модель SQLAlchemy для сущности,
# также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)

from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(500))
    trailer = db.Column(db.String(250))
    year = db.Column(db.Integer)
    rating = db.Column(db.String(50))
    genre_id = db.Column(db.Integer)
    director_id = db.Column(db.Integer)

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre_id = fields.Int()
    director_id = fields.Int()
