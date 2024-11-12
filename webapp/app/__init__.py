from flask import Flask
from .config import config
from .models.db import init_db
from .models.device import Device
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    settings = config[config_name]

    
    init_db(app, settings)
   
    from .main import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

   

    from .device import device as device_bp
    app.register_blueprint(device_bp, url_prefix='/devices')
    
    

    return app