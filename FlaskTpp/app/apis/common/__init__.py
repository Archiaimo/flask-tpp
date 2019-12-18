from flask_restful import Api
from app.apis.common.city_api import CitiesResource
from app.apis.common.movie_api import MoviesResource, MovieResource

common_api=Api(prefix='/common')
common_api.add_resource(CitiesResource,'/cities/')
common_api.add_resource(MoviesResource,'/movies/')
common_api.add_resource(MovieResource,'/movives/<int:id>')