from flask import Flask
app = Flask(__name__)
app.secret_key = "Secret_key"
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
from test import routes