from flask import render_template, Blueprint

bp = Blueprint("client", __name__)

@bp.route("/")
def home():
    return render_template("home.html")