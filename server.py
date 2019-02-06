#!flask/bin/python
from flask import Flask
from flask import jsonify
import time
app = Flask(__name__)

@app.route('/')
def index():
    return "Please go to /time for the API"


@app.route('/time', methods=['GET'])
def get_tasks():
    return jsonify({'time': time.time()})

if __name__ == '__main__':
    app.run(debug=True)
