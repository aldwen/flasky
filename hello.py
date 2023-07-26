from flask import Flask
from flask import make_response
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template
from flask import session
from flask import flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

bootstrap = Bootstrap(app)
moment= Moment(app)

app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'WHEN YOU SEE YOU WOULD DIE'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    submit = SubmitField ('提交')

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name= session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('看起来你改了名字')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    else:
        return render_template('index.html',form=form, name=session.get('name'))

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
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500