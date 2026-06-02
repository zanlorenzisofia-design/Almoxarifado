from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/inicio')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
