from flask import Flask, jsonify, render_template
from . import main as bp

@bp.route('/')
def home():
    
    return  render_template('index.html', bp_name='main')
    