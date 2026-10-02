from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route("", methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)
