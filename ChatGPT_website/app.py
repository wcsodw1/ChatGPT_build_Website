from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Get list of all PNG images in static folder
    png_images = [f for f in os.listdir('static') if f.endswith('.jpg')]

    # Select a random PNG image
    selected_image = random.choice(png_images)

    # Add selected image to index.html and return
    return render_template('index.html', image=selected_image)

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/hotel')
def hotel():
    return render_template('hotel.html')

if __name__ == '__main__':
    app.run()