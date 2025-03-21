""" 
Configuration for the backend application.
"""
import os

class Config:
    DEBUG = True
    # AWS Database configuration (replace with your free-tier AWS DB settings)
    DB_HOST = os.environ.get("AWS_DB_HOST", "your-db-host.amazonaws.com")
    DB_PORT = os.environ.get("AWS_DB_PORT", "5432")
    DB_NAME = os.environ.get("AWS_DB_NAME", "predictive_db")
    DB_USER = os.environ.get("AWS_DB_USER", "dbuser")
    DB_PASSWORD = os.environ.get("AWS_DB_PASSWORD", "dbpassword")
