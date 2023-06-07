from flask import Flask, render_template, request, url_for, redirect, abort
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario', methods=['POST', 'GET'])
def form():
    return redirect(url_for('index'))
    # print(request.form)
    # print(request.form['llave1'])
    # return request.form['llave2']

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/aborto', methods=['GET', 'POST'])
def aborto():
    abort(401)

@app.route('/json', methods=['GET', 'POST'])
def json():
    return {
        "user": "wenardo",
        "pass": "pelao",
        "suenos": "tener pelo"
    }
