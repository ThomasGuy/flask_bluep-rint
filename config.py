import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET') or 'secret'
    SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME') or 'cookie'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////c/data/sqlite/db/bfx_serverDB.db" or None


# # open a WSL terminal.

# # Create and modify the new WSL configuration file:
# sudo nano /etc/wsl.conf

# # To remove /mnt/c/ from wsl windows paths, so all windows paths start /c/:
# # make wsl.conf look like this:-
# [automount]
# root = /
# options = "metadata"
