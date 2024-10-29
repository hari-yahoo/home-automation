from flask import Flask
from .config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #config[config_name].init_app(app)

    #db.init_app(app)


    from .main import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/main')

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .api import api as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


    return app