from flask import Flask, jsonify, render_template
from . import main as bp
from app.models.base import db
from app.models.device import Device


@bp.route('/')
def home():
    # if app.config["INIT_FAILED"]:
    #     return render_template("error.html", message="Hardware initialization failed.")
    devices = db.session.execute(db.select(Device).order_by(Device.name)).scalars()
    return  render_template('index.html', devices=devices)
    