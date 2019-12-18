from app.ext import db
from app.models import BaseModel
from app.models.cinema_admin.cinema_hall_model import Hall
from app.models.common.movie_model import Movie


class HallMovie(BaseModel):
    h_movie_id=db.Column(db.Integer,db.ForeignKey(Movie.id))
    h_hall_id=db.Column(db.Integer,db.ForeignKey(Hall.id))
    h_time=db.Column(db.DateTime)

    h_orders = db.relationship('MovieOrder', backref='HallMovie', lazy=True)
