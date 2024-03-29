from werkzeug.security import generate_password_hash, check_password_hash

from app.models import BaseModel
from app.ext import db
from app.models.movie_user.model_constant import PERMISSION_NONE

COMMON_USER=0
BLACK_USER=1
VIP_USER=2

class CinemaUser(BaseModel):
    username=db.Column(db.String(32),unique=True)
    _password=db.Column(db.String(256))
    phone=db.Column(db.String(32),unique=True)
    is_delete=db.Column(db.Boolean,default=False)
    is_verify = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise Exception("can't access")

    @password.setter
    def password(self,password_value):
        self._password=generate_password_hash(password_value)

    def check_password(self,password_value):
        return check_password_hash(self._password,password_value)

    def check_permission(self,permission):

        if not self.is_verify:
            return False

        permissions=CinemaUserPermission.query.filter_by(c_user_id=self.id)
        for user_permission in permissions:
            if permission == Permissions.query.get(user_permission.c_permission_id).p_name:
                return True
        return False

class Permissions(BaseModel):
    p_name=db.Column(db.String(64),unique=True)

class CinemaUserPermission(BaseModel):
    c_user_id=db.Column(db.Integer,db.ForeignKey(CinemaUser.id))
    c_permission_id = db.Column(db.Integer, db.ForeignKey(Permissions.id))

