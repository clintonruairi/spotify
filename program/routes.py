from program import app
from flask import render_template

@app.route('/')
def index():
    return "This is my Spotify app"
