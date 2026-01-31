"""Flask application for Vercel serverless deployment."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return a greeting message."""
    return "Hello, World!"


@app.route("/<path:path>")
def catch_all(path):
    """Catch-all route for any other paths."""
    return "Hello, World!"
