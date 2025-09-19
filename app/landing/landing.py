from flask import render_template, redirect, url_for, request
from . import landing_bp

@landing_bp.route("/")
def landing():
    return render_template("landing.html")