#!/usr/bin/env python3
"""A simple Hello World Flask application."""

import logging
import sys

from flask import Flask

# Configure logging for Vercel deployment
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

logger.info("Flask app initialized")


@app.route("/")
def home():
    """Return a greeting message."""
    logger.debug("Home route accessed")
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
