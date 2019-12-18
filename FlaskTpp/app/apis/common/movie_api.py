from flask import request
from flask_restful import Resource, reqparse, abort, fields, marshal, marshal_with
from werkzeug.datastructures import FileStorage

from app.apis.admin.admin_utils import login_required
from app.apis.api_constant import HTTP_CREATE_OK, HTTP_OK
from app.apis.common.utils import filename_transfer
from app.models.common.movie_model import Movie
from app.settings import UPLOADS_DIR, FILE_PATH_PREFIX

parse=reqparse.RequestParser()
parse.add_argument('showname',type=str,required=True,help='请输入电影名字')
parse.add_argument('shownameen',type=str,required=True,help='请输入电影英文名字')
parse.add_argument('director',type=str,required=True,help='请输入电影导演')
parse.add_argument('leadingRole',type=str,required=True,help='请输入电影主演')
parse.add_argument('type',type=str,required=True,help='请输入电影类型')
parse.add_argument('country',type=str,required=True,help='请输入国家')
parse.add_argument('language',type=str,required=True,help='请输入语言')
parse.add_argument('duration',required=True,help='请输入电影时长')
parse.add_argument('screeningmodel',type=str,required=True,help='请输入电影荧幕')
parse.add_argument('openday',required=True,help='请输入电影上映日期')
parse.add_argument('backgroundpicture',type=FileStorage,required=True,help='请输入电影海报',
                   location=['file'])

movie_fields={
    'showname':fields.String,
    'shownameen':fields.String,
    'director': fields.String,
    'leadingRole': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.Integer,
    'screeningmodel': fields.String,
    'openday': fields.DateTime,
    'backgroundpicture': fields.String,

}
multi_movies_fields={
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.List(fields.Nested(movie_fields))
}

class MoviesResource(Resource):

    @marshal_with(multi_movies_fields)
    def get(self):
        movies=Movie.query.all()
        data={
            'msg':'ok',
            'status':HTTP_OK,
            'data':movies
        }
        return data

    @login_required
    def post(self):
        args=parse.parse_args()

        showname=args.get('showname')
        shownameen = args.get('shownameen')
        director = args.get('director')
        leadingRole = args.get('leadingRole')
        m_type = args.get('type')
        country = args.get('country')
        language = args.get('language')
        duration = args.get('duration')
        screeningmodel = args.get('screeningmodel')
        openday = args.get('openday')
        backgroundpicture = args.get('backgroundpicture')
        #backgroundpicture = request.files.get('backgroundpicture')

        movie=Movie()
        movie.showname=showname
        movie.shownameen=shownameen
        movie.director=director
        movie.leadingRole=leadingRole
        movie.type=m_type
        movie.country=country
        movie.language=language
        movie.duration=duration
        movie.screeningmodel=screeningmodel
        movie.openday=openday

        file_info=filename_transfer(backgroundpicture.filename)
        filepath=file_info[0]

        backgroundpicture.save(filepath)
        movie.backgroundpicture=file_info[1]

        if not movie.save():
            abort(400,msg='can not create movie')
        data={
            'msg':'create success',
            'status':HTTP_CREATE_OK,
            'data':marshal(movie,movie_fields)
        }
        return {'msg':'post ok'}

class MovieResource(Resource):
    def get(self):
        movie=Movie.query.get(id)
        if not movie:
            abort(404,msg='movie is not exist')
        data={
            'msg':'ok',
            'status':HTTP_OK,
            'data':marshal(movie,movie_fields)
        }
        return data

    @login_required
    def patch(self,id):
        return {'msg':'post ok'}

    @login_required
    def put(self,id):
        return {'msg':'post ok'}

    @login_required
    def delete(self,id):
        return {'msg':'post ok'}