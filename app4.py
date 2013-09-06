#!/usr/bin/env python

from flask import Flask, render_template, redirect, session, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    # How can we customize this message with the session?
    return render_template('hello.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    # How can we make this dynamic?
    session['user'] = 'Rafe'
    return redirect(url_for("hello"))

@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for("hello"))

app.secret_key = '1ohNxwC9QF7vrIN83EI1dd6HYeTzlRrZ'

if __name__ == "__main__":
    app.run(debug=True)
