import os

class Config(object):
    SECRET_KEY=os.getenv('SECRET') or 'secret'
    SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME') or 'cookie'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////c/data/sqlite/db/blast_DB.db" or None
