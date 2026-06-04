from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/inicio')
def home():
    return render_template('home.html')

@app.route('/estoque')
def estoque():  # Alterado de home para estoque
    return render_template('estoque.html')

if __name__ == '__main__':
    app.run(debug=True)