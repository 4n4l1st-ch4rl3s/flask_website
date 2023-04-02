from flask import Flask
import website.config as config

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config.secret_key

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app