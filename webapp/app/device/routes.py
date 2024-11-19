from flask import Flask, jsonify, redirect, render_template, url_for, request

from app.hardware.feeder import Feeder
from app.hardware.light import Light
from app.hardware.initializer import Initializer
from app.models.db import db
from app.models.device import Device

from . import device as bp


@bp.route("/list", methods=["GET"])
def list():
    devices = db.session.execute(db.select(Device).order_by(Device.name)).scalars()
    return render_template('list.html', devices=devices)


@bp.route("/", methods=["GET"])
def new_device():
    device = Device()  # Create a new device object to pass to the form template
    return render_template("details.html", device=device)

@bp.route("/", methods=["POST"])
def create():
    device = Device(
        name=request.form["name"],
        device_type=request.form["dtype"],
        pin=request.form["pin"],
        location=request.form["location"],
        state=False,
    )
    db.session.add(device)
    db.session.commit()
    return jsonify({"status" : "done"})

@bp.route("/<int:id>", methods=["GET"])
def retrieve(id):
    device = db.session.get(Device, id)
    if device:
        return render_template("details.html", device=device)
    else:
        return jsonify({"error": "Device not found"}), 404

@bp.route("/<int:id>", methods=["PUT"])
def update(id):
    device = db.session.get(Device, id)
    if device:
        device.name = request.form["name"]
        device.device_type = request.form["dtype"]
        device.pin = request.form["pin"]
        device.location = request.form["location"]
        db.session.commit()

    return jsonify({"status" : "done"})

@bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    pass    

@bp.route("/<int:id>/<action>", methods=["PUT"])
def turn_on(id, action):
    #device = Device.query.get(id)
    device = db.session.get(Device, id)
    print(device.name, device.pin)
    if device:
        dtype = device.device_type.lower()

        if dtype == "light":
            light = Light(Initializer.arduino, pin = device.pin)
            light.on() if action == "on" else light.off()
        elif dtype == "pump":
            print("Pumb")
        elif dtype == "feeder":
            feeder = Feeder(Initializer.arduino, pin = device.pin)
            feeder.feed() if action == "on" else feeder.off()
        else:
            print(f"Unsupported device type: {dtype}")

        device.state = (action == 'on')
        db.session.commit()

    return jsonify({"status" : "on"})

@bp.route("/<int:pin>/turn")
def servo_test(pin):
    duration = request.args.get('duration')
    angle = request.args.get('angle')
    print(angle)
    print(duration)
    
    feeder = Feeder(Initializer.arduino, pin = pin)
    feeder.feed_fast(duration=duration, angle=angle)
    return jsonify({"status" : "on"})
