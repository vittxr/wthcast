import os 
import app
from flask import Flask 

def create_app():
    app = Flask(__name__)

    from app.main import main as main_bp
    app.register_blueprint(main_bp)
       #é preciso fazer o registro da blue print no app!

    return app