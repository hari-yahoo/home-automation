
from .base import *


class Device(Base):
    __tablename__ = 'devices'
        
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    device_type = db.Column(db.String(50), nullable=False)
    location= db.Column(db.String(100))
    pin = db.Column(db.Integer, default=1)
    state = db.Column(db.Boolean, default=False)
    schedule = db.Column(db.Boolean, default=False)
