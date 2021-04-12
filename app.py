from flask import Flask, render_template, request, url_for, redirect
from Core import Password_generator
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from flask_login import *

password_generator = Password_generator()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/nonserver', methods=["POST", "GET"])
def nonserver_page():
    global password_generator
    if request.method == "GET":
        return render_template("nonserver.html")
    elif request.method == "POST":
        url = request.form["url"]
        username = request.form["username"]
        secret_pass = request.form["password"]
        generated_pass = password_generator.generate(user_name=username, secret_pass=secret_pass, url=url, color="")
        return render_template("generated.html", password=generated_pass)  # TODO


@app.route('/faq')
def faq():
    return "", 404  # TODO


@app.route('/cloud')
def cloud():
    pass  # TODO


@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
  if g.user is not None and g.user.is_authenticated():
      return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit():
      session['remember_me'] = form.remember_me.data
      return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
  return render_template('login.html',
      title = 'Sign In',
      form = form,
      providers = app.config['OPENID_PROVIDERS'])

@app.route('/register')
def reg_page():
    pass  # TODO


@app.route('/logout')
def logout():
    pass  # TODO


if __name__ == '__main__':
    app.run(debug=True)
