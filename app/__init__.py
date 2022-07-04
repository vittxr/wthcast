import app
from flask import Flask 
from config import config

def create_app(config_name):
   app = Flask(__name__)
   app.config.from_object(config[config_name])

   from app.main import main as main_bp
   app.register_blueprint(main_bp)
       #é preciso fazer o registro da blue print no app!

   return app