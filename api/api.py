import time
from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/time')
def get_current_time():
    return { 'time': time.time() }