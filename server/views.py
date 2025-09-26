from flask import Blueprint, redirect, url_for

server = Blueprint("server", __name__)


@server.route("/")
def home():
    return redirect(url_for(".connect"))


@server.route("/connect")
def connect():
    return {"hello": "world"}