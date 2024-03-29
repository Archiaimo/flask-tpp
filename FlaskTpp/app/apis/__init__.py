from app.apis.admin import admin_api
from app.apis.common import common_api
from app.apis.cinema_admin import cinema_client_api
from app.apis.movie_user import client_api

def init_api(app):
    client_api.init_app(app)
    cinema_client_api.init_app(app)
    admin_api.init_app(app)
    common_api.init_app(app)

