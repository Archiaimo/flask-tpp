from datetime import datetime,timedelta

from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal
from sqlalchemy import or_

from app.apis.api_constant import HTTP_CREATE_OK
from app.apis.movie_user.models_utils import get_movie_user, login_required, require_permission
from app.models.cinema_admin.cinema_hall_model import Hall
from app.models.cinema_admin.cinema_hall_movie_model import HallMovie
from app.models.movie_user.movie_order_model import MovieOrder, ORDER_STATUS_PAYED_NOT_GET, ORDER_STATUS_GET, \
    ORDER_STATUS_NOT_PAY
from app.models.movie_user.movie_user_model import VIP_USER

parse=reqparse.RequestParser()
parse.add_argument('token',required=True,help='请登录')
parse.add_argument('hall_movie_id',required=True,help='请提供排挡信息')
parse.add_argument('o_seats',required=True,help='请正确选择座位')

movie_order_fields={
    'o_price':fields.Float,
    'o_seats':fields.String,
    'o_hall_movie_id':fields.Integer
}

class MovieOrdersResource(Resource):

    @login_required
    def post(self):
        args=parse.parse_args()
        hall_movie_id=args.get('hall_movie_id')
        o_seats=args.get('o_seats')

        # 订单筛选，排挡筛选，订单状态，锁单的
        movie_orders_buyed = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(
            or_(MovieOrder.o_status == ORDER_STATUS_PAYED_NOT_GET,
                MovieOrder.o_status == ORDER_STATUS_GET)).all()
        movie_order_lock = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(
            MovieOrder.o_status == ORDER_STATUS_NOT_PAY).filter(MovieOrder.o_time > datetime.now()).all()
        seats = []
        for movie_orders in movie_orders_buyed:
            sold_seats = movie_orders.o_seats.split('#')
            seats += sold_seats
        for movie_orders in movie_order_lock:
            sold_seats = movie_orders.o_seats.split('#')
            seats += sold_seats

        hall_movie=HallMovie.query.get(hall_movie_id)
        hall=Hall.query.get(hall_movie.h_hall_id)
        all_seats = hall.h_seats.split('#')
        can_buy = list(set(all_seats) - set(seats))
        want_buy=o_seats.split('#')
        for item in want_buy:
            if item not in can_buy:
                abort(400,msg='锁座失败')

        user=g.user

        movie_order=MovieOrder()
        movie_order.o_hall_movie_id=hall_movie_id
        movie_order.o_seats=o_seats
        movie_order.o_user_id=user.id
        movie_order.o_time=datetime.now() + timedelta(minutes=15)

        if not movie_order.save():
            abort(400,msg='下单失败')
        data={
            'msg':'success',
            'status':HTTP_CREATE_OK,
            'data':marshal(movie_order,movie_order_fields)
        }
        return data

class MovieOrderResource(Resource):

    @require_permission(VIP_USER)
    def put(self,order_id):
        return {'msg':'change success'}