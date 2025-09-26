from flask import Flask, redirect
from werkzeug.middleware.dispatcher import DispatcherMiddleware

import client
import server

if __name__ == "__main__":
    client_app = client.create_app()
    server_app = server.create_app()

    app = Flask(__name__)
    app.wsgi_app = DispatcherMiddleware(
        app,
        mounts={
            "/server": server_app,
            "/web": client_app,
        },
    )

    @app.route("/")
    def home():
        return {"hello": "world"}

    app.run(debug=True)