import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'blablastring'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
		
class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class TestConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-prod.sqlite')
	
config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
    'test': TestConfig,
	'default': DevelopmentConfig
}