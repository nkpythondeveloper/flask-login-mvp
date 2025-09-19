from flask import render_template, redirect, url_for, request, flash
from ..extensions import db
from ..models import User
from ..forms import RegisterUserForm, LoginUserForm
from flask_login import login_required, login_user, logout_user, current_user
from . import auth_bp


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("logic.dashboard"))
    form = RegisterUserForm()
    if form.validate_on_submit():
        new_user = User(
            first_name = form.first_name.data.strip(),
            last_name = form.last_name.data.strip(),
            email_id = form.email_id.data.strip()
        )
        new_user.set_password(form.password.data.strip())
        if User.query.filter_by(email_id=new_user.email_id).first():
            flash("User already exists!", "danger")
        else:
            db.session.add(new_user)
            db.session.commit()
            flash("Registration Successful! Now log in !", "success")
            return redirect(url_for("auth.login"))
    
    return render_template("register_user.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginUserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email_id=form.email_id.data.strip()).first()
        if user and user.check_password(form.password.data.strip()):
            login_user(user)
            flash("Login Successfully!", "success")
            return redirect(url_for("logic.dashboard"))
        else:
            flash("Invalid Credentials!", "danger")
    return render_template("login_user.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successful!", "danger")
    return redirect(url_for("auth.login"))