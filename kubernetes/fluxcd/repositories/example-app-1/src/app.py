from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Thinh Nguyen! v1.0.0.2"