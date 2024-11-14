from flask import Flask, render_template

from app.hardware.initializer import Initializer
from .config import config
from .models.db import init_db
from .models.device import Device

initialized = False

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    settings = config[config_name]

    init_db(app, settings)
    
    from .main import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/')


    if init_hardware():
        from .device import device as device_bp
        app.register_blueprint(device_bp, url_prefix='/devices')
    else:
        app.config["INIT_FAILED"] = True
        raise 

    @app.errorhandler(500)
    def handle_internal_error(e):
        if app.config.get("INIT_FAILED"):
            return render_template("error.html", message="System initialization failed.")
        return render_template("error.html", message="An internal error occurred.")
        
    
    import atexit

    atexit.register(exit_gracefully)
    
    return app

def init_hardware():
    # Initialize hardware components, e.g., GPIO pins, serial connections, etc.
    
    global initialized

    result = True
    if not initialized:
        # Perform initialization here
        initialized = True

        if Initializer.arduino == None:
            initializr = Initializer()
            result = initializr.initialize_board()

        print("Init Hardware invoked")
    return result

def exit_gracefully():
    print("Exiting gracefully...")
    # Close all hardware connections and release resources
    if Initializer.arduino:
        Initializer.arduino.close()
    