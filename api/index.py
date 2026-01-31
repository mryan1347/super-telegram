"""Vercel serverless function entry point for Flask app."""

from app import app

# Vercel expects the WSGI app to be named 'app' or 'application'
# This file serves as the entry point for the serverless function
