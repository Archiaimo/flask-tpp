from flask_restful import Api

from app.apis.movie_user.movie_hall_api import UserMovieHallsResource, UserMovieHallResource
from app.apis.movie_user.movie_order_api import MovieOrderResource, MovieOrdersResource
from app.apis.movie_user.movie_order_pay_api import MovieOrderPayResource
from app.apis.movie_user.movie_top_api import MovieTopResource
from app.apis.movie_user.movie_user_api import MovieUsersResource

client_api=Api(prefix='/user')

client_api.add_resource(MovieUsersResource,'/movieuser/')
client_api.add_resource(MovieOrdersResource,'/movieorders/')
client_api.add_resource(MovieOrderResource,'/movieorders/<int:order_id>/')
client_api.add_resource(UserMovieHallsResource, '/moviehalls/')
client_api.add_resource(UserMovieHallResource, '/moviehalls/<int:id>/')
client_api.add_resource(MovieOrderPayResource, '/movieorderpay/<int:order_id>/')
client_api.add_resource(MovieTopResource, '/movietop/')