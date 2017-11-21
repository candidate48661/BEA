import os


# IMPORTANT! Replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="cpTest", DB_PASS="cpTestPass", DB_ADDR="127.0.0.1", DB_NAME="accounts")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')