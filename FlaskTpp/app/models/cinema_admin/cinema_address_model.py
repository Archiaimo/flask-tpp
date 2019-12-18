from app.ext import db
from app.models import BaseModel
from app.models.cinema_admin.cinema_user_model import CinemaUser


class CinemaAddress(BaseModel):
    c_user_id=db.Column(db.Integer,db.ForeignKey(CinemaUser.id))
    name=db.Column(db.String(64))
    city=db.Column(db.String(16))
    district=db.Column(db.String(16))
    address=db.Column(db.String(28))
    phone=db.Column(db.String(32))
    score=db.Column(db.Float,default=10)
    hallnum=db.Column(db.Integer,default=1)
    servicecharge=db.Column(db.Float,default=10)
    astrict=db.Column(db.Float,default=10)
    flag=db.Column(db.Boolean,default=False)
    is_delete=db.Column(db.Boolean,default=False)
