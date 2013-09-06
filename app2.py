#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # Intentionally trigger a TypeError. Why is this an error?
    i = 3
    return "Hello World!" + i

if __name__ == "__main__":
    app.run(debug=True)
