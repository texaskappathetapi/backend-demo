import os

class Config(object):
  SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
  DEBUG = os.environ.get("DEBUG", True)
  SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///butter.db")
  SQLALCHEMY_TRACK_MODS = False
  