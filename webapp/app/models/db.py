from .base import db
from .device import Device


def init_db(app, settings):
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URI
    
    db.init_app(app)
        
    with app.app_context():
        db.create_all()
        devices = db.session.execute(db.select(Device).order_by(Device.name)).scalars()

        
