import os

class Config ():
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SSL_REDIRECT = False 

    @staticmethod 
    def init_app(app):
      pass 


class DevelopmentConfig(Config): 
    DEBUG = True  

class ProductionConfig(Config):
    DEBUG = False  

    @staticmethod
    def init_app(app):
      import logging  
      from logging import FileHandler

      handler = FileHandler("log.log", "a")
      handler.setLevel(logging.INFO)
      app.logger.addHandler(handler)
         #O heroku não terá debug, então se faz um arquivo para armazenar os erros quando eles aparecerem.

      from werkzeug.middleware.proxy_fix import ProxyFix 
      app.wsgi_app = ProxyFix(app.wsgi_app)

class HerokuConfig(ProductionConfig):
      SSL_REDIRECT = True if os.getenv("DYNO") else False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': Config,
    'heroku': HerokuConfig
}