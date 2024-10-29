from flask import Flask, jsonify, render_template
from . import api as bp

@bp.route('/')
def home():
    
    info = { 'message' : 'API Home'}
    return jsonify(info)
    