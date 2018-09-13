import os


class Config:
    '''
    General config parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://renegade:pitch@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class TestConfig(Config):
    '''
    containers all the congigure for test
    '''


class ProdConfig(Config):
    '''
    Production congig for child
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
