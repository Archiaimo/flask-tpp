from flask_restful import Resource
from sqlalchemy import func

from app.ext import db
from app.models.cinema_admin.cinema_hall_movie_model import HallMovie
from app.models.common.movie_model import Movie
from app.models.movie_user.movie_order_model import MovieOrder


class MovieTopResource(Resource):
    def get(self):
        #数据查询的原生写法
        results=db.session.query(Movie.id,Movie.showname,func.sum(MovieOrder.o_price)).\
            join(Movie.hall_movies).join(HallMovie.h_orders).\
            group_by(Movie.id).order_by(-func.sum(MovieOrder.o_price))


        for result in results:
            print(result)
        data={
            'msg':'ok',
        }
        return data