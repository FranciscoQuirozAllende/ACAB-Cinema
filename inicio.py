from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'puta la wea que tengo pena'