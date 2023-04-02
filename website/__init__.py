from flask import Flask
import website.config as config

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config.secret_key

    return app