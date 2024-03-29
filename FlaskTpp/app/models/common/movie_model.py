from app.ext import db
from app.models import BaseModel


class Movie(BaseModel):
    __tablename__='movies'
    showname=db.Column(db.String(64))
    shownameen=db.Column(db.String(128))
    director=db.Column(db.String(64))
    leadingRole=db.Column(db.String(256))
    type=db.Column(db.String(64))
    country=db.Column(db.String(64))
    language=db.Column(db.String(64))
    duration=db.Column(db.Integer,default=90)
    screeningmodel=db.Column(db.String(32))
    openday=db.Column(db.DateTime)
    backgroundpicture=db.Column(db.String(256))
    flag=db.Column(db.Boolean,default=False)
    is_delete = db.Column(db.Boolean, default=False)
    #反向引用
    hall_movies=db.relationship('HallMovie',backref='Movie',lazy=True)