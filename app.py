import json
from flask import Flask, render_template

app = Flask(__name__)

MAPS_API_KEY = ''

@app.route('/')
def index():
    with open('teachers.json') as f:
        teachers = json.load(f)

    return render_template('index.html', teachers=teachers, maps_api_key=MAPS_API_KEY)
