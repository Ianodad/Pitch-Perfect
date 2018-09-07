import os


class Config:
    '''
    General config parent class
    '''
    pass

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://renegade:pitch@localhost/pitch'


class TestConfig(Config):
    '''
    containers all the congigure for test
    '''


class ProdConfig(Config):
    '''
    Production congig for child 
    '''
    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
