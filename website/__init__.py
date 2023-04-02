from flask import Flask
import config_file

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config_file.secret_key

    return app