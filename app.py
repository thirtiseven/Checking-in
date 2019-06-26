from flask import Flask
from flask_bootstrap import Bootstrap

from Checking_in import app, db, login_manager

if __name__ == '__main__':
    app = Flask(__name__)
    login_manager.login_view = 'login'
    Bootstrap(app)
    app.run()
