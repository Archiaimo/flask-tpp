import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALIPAY_APPID=''
APP_PRIVATE_KEY=open(os.path.join(BASE_DIR,'alipay_config/app_rsa_private_key.pem'),'r').read()
ALIPAY_PUBLIC_KEY=open(os.path.join(BASE_DIR,'alipay_config/alipay_rsa_public_key.pem'),'r').read()

def get_db_uri(dbinfo):
    engine=dbinfo.get('engine')
    driver=dbinfo.get('driver')
    user=dbinfo.get('user')
    password=dbinfo.get('password')
    host=dbinfo.get('host')
    port=dbinfo.get('port')
    name=dbinfo.get('name')
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine,driver,user,password,host,port,name)

class Config:
    DEBUG=False
    TESTING=False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='secret'

class DevelopConfig(Config):
    DEBUG = True
    dbinfo={
        'engine':'mysql',
        'driver':'mysqlconnector',
        'user':'root',
        'password':'Archi920328!',
        'host':'localhost',
        'port':'3306',
        'name':'flasktpp',
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class TestConfig(Config):
    Testing = True
    dbinfo={
        'engine':'mysql',
        'driver':'pymysql',
        'user':'root',
        'password':'Archi920328!',
        'host':'localhost',
        'port':'3306',
        'name':'flasktpp',
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class StagineConfig(Config):
    dbinfo={
        'engine':'mysql',
        'driver':'pymysql',
        'user':'root',
        'password':'Archi920328!',
        'host':'localhost',
        'port':'3306',
        'name':'flasktpp',
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)

class ProductConfig(Config):
    dbinfo={
        'engine':'mysql',
        'driver':'pymysql',
        'user':'root',
        'password':'Archi920328!',
        'host':'localhost',
        'port':'3306',
        'name':'flasktpp',
    }
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)
envs={
    'develop':DevelopConfig,
    'testing':TestConfig,
    'stagine':StagineConfig,
    'product':ProductConfig,
    'default':DevelopConfig,
}

ADMINS=('aimo','AIMO','aina')

FILE_PATH_PREFIX='/static/uploads/icons'
UPLOADS_DIR=os.path.join(BASE_DIR,'app/static/uploads/icons')