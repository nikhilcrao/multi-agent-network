from flask import Flask, redirect
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

import client
import server

if __name__ == "__main__":
    client_app = client.create_app()
    server_app = server.create_app()

    app = Flask(__name__)
    app.wsgi_app = DispatcherMiddleware(
        NotFound(),
        mounts={
            "/server": server_app,
            "/web": client_app,
        },
    )
    app.run(debug=True, port=5001)