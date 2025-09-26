from flask import Flask

from .views import server


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(server)
    return app