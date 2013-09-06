#!/usr/bin/env python

import redis
from flask import Flask, render_template, redirect, session, url_for, g
app = Flask(__name__)

@app.before_request
def connect_db():
    g.db = redis.Redis()

@app.teardown_request
def disconnect_db():
    g.db.close()

@app.route("/")
def hello():
    # Our first query!
    count = g.db.incr('visits')
    # How can we customize this message for a logged in user?
    return render_template('hello2.html', visits=count)

@app.route("/login", methods=["GET", "POST"])
def login():
    # How can we record the user that logged in?
    return redirect(url_for("hello"))

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for("hello"))

app.secret_key = '1ohNxwC9QF7vrIN83EI1dd6HYeTzlRrZ'

if __name__ == "__main__":
    app.run(debug=True)
