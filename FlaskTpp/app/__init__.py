from flask import Flask

from app.apis import init_api
from app.ext import init_ext
from app.settings import envs


def create_app(env):
    app=Flask(__name__,template_folder='../templates') #设置模板文件夹相对路径
    app.config.from_object(envs.get(env))
    init_ext(app)
    init_api(app)

    return app