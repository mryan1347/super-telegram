#!/usr/bin/env python3
"""A simple Hello World Flask application."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return a greeting message."""
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
