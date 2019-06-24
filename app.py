from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from Checking_in import app, db

if __name__ == '__main__':
    app = Flask(__name__)
    Bootstrap(app)
    app.run()
