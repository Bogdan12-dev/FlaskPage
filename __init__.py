from flask import Flask
app = Flask(__name__)
app.secret_key = "Secret_key"
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
from test import routes
https://docs.google.com/forms/d/e/1FAIpQLSdIwn_eaq0HGwqqUKbEG8iYznn24HhRjT0LG6zDdl4hlu2OPA/viewform?usp=sharing
