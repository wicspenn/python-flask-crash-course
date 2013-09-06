#!/usr/bin/env python

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello world!"

@app.route("/<name>/<int:number>")
def answer(name, number):
    correct = number == 42
    # How can we improve the page we rendered?
    return render_template('answer.html',
      name=name, correct=correct)

if __name__ == "__main__":
    app.run(debug=True)
