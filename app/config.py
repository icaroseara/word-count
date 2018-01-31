import os
from app import app

class Config(object):
    DEBUG = False
    TESTING = False
    PRODUCTION = False


class Development(Config):
    MODE = 'Development'
    DEBUG = True
    SECRET_KEY = 'secret_key'


class Production(Config):
    MODE = 'Production'
    DEBUG = False
    PRODUCTION = True
    SECRET_KEY = 'secret_key' # os.environ['SECRET_KEY']

flask_config = os.environ.get('FLASK_CONFIG', 'Development')
app.config.from_object('app.config.{}'.format(flask_config))
