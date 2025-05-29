import os
from flask import Flask, redirect, url_for
from flask_cors import CORS
from services import _register_blueprints, _register_error_handlers
import importlib

# App factory baseado no artigo em: 
# https://medium.com/@ferrohardian/application-factory-pattern-starting-your-flask-project-e17dd2f12013

def create_app(test_config=None):
    # Factory que cria a aplicação Flask
    app = Flask(__name__)
    _set_session_default_data(app)
    _register_blueprints(app, 'configs.toml')
    _register_error_handlers(app)
    CORS(app)
    
    return app
    
def _set_session_default_data(app):
    app.config['SECRET_KEY'] = '3ADD1982CE3B39DBE0A2F12520C976EA73B9DF113CD1B0C74014AF37839BA4FF'
    app.config['SESSION_PERMANENT'] = False