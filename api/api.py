import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/api/v1/time')
def get_current_time():
    return { 'time': time.time() } 