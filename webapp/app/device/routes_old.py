from flask import Flask, jsonify, redirect, render_template, url_for, request

from app.models.device import Device
from app.models.db import db
from .controls import control_device

from . import device as bp

@bp.route('/')
def index():
    #devices = Device.query.all()
    devices = db.session.execute(db.select(Device).order_by(Device.name)).scalars()
    return render_template('list.html', devices=devices)

@bp.route('/control/<device_id>/<action>')
def control(device_id, action):
    device = Device.query.get(device_id)
    if device:
        control_device(device.name, action)
        device.state = (action == 'on')
        db.session.commit()
    return redirect(url_for('index'))



@bp.route("/create", methods=["GET", "POST"])
def device_create():
    if request.method == "POST":
        device = Device(
            name=request.form["name"],
            location=request.form["location"],
        )
        db.session.add(device)
        db.session.commit()
        return redirect(url_for("/devices", id=device.id))
    # else:
    #     return render_template("details.html")

    return render_template("details.html")