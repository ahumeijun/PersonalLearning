#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action='/signin' method='post'>
                <p><input name="username"></p>
                <p><input name="password" type="password"></p>
                <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'whosyourdaddy':
        return '<h2>Hello, %s!<h2>'%username
    else:
        return '<h3>user name or password not correct!</h3>'


if __name__ == '__main__':
    print('****')
    app.run()