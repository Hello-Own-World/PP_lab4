from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/hello-world-30')
def hello_world():
    return 'Hello, World 30', 200
