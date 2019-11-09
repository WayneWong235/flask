import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'notejam-flask-secret-key'
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'notejam-flask-secret-key'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'notejam.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ['DB_USERNAME'] + ':' +os.environ['DB_PASSWD'] + '@demoflask.ctotioexeoyh.ap-southeast-1.rds.amazonaws.com:3306/demoflask?charset=utf8mb4&use_unicode=0'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
