from flask import request,g
from flask_restful import abort

from app.ext import cache
from app.models.admin.admin_user_model import AdminUser
from app.utils import ADMIN_USER


def _verify():
    token = request.args.get('token')
    if not token:
        abort(401, msg='not login')

    if not token.startswith(ADMIN_USER):
        abort(403,msg='no access')

    user_id = cache.get(token)
    if not user_id:
        abort(401, msg='user not avaliable')
    user = get_admin_user(user_id)
    if not user:
        abort(401, msg='user not avaliable')
    g.user = user
    g.auth = token

def get_admin_user(user_ident):
    if not user_ident:
        return None

    #根据id查找
    user=AdminUser.query.get(user_ident)
    if user:
        return user

    #根据用户名查找
    user=AdminUser.query.filter(AdminUser.username==user_ident).first()
    if user:
        return user
    return None

def login_required(fun):
    def wrapper(*args,**kwargs):
        _verify()
        return fun(*args,**kwargs)
    return wrapper

def require_permission(permission):
    def require_permission_wrapper(fun):
        def wrapper(*args,**kwargs):
            _verify()
            if not g.user.check_permission(permission):
                abort(403,msg='user can not access')
            return fun(*args,**kwargs)
        return wrapper
    return require_permission_wrapper