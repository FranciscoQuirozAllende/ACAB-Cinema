from flask import Flask, render_template
import mysql.connector
bd = mysql.connector.connect(host="localhost",
                             password="Hola1hola",
                             user="Mauro",
                             database="penelope")
cursor = bd.cursor(dictionary=True)

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/poto')
def caca():
    cursor.execute('select * from aquiles;')
    guardarcosas = cursor.fetchall()
    return render_template('nuebo.html', pruea=guardarcosas)