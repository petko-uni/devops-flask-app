from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<a href="/about">/about</a>'


@app.route('/about')
def say_hello():
    return '<p>Test, I am a Flask app!</p>'
