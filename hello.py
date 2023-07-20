from flask import Flask
from flask import make_response
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

@app.route('/redirect')
def movetoindex():
    return redirect(url_for('index'))

@app.route('/aaa')
def get_user():
    abort(403)