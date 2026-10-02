from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Session, Message, db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    name = data.get("name", "User")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    user = User(name=name, email=email, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()

    login_user(user)
    return jsonify({"message": "Registered successfully", "user": user.to_dict()}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        login_user(user)
        return jsonify({"message": "Logged in", "user": user.to_dict()})

    return jsonify({"error": "Invalid credentials"}), 401

@bp.route("/guest", methods=["POST"])
def guest_login():
    name = request.get_json().get("name", "Guest Developer")
    guest_email = f"guest_{abs(hash(name + str(__import__('time').time())))}@guest.local"
    user = User(name=name, email=guest_email, password_hash="", is_guest=True)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return jsonify({"message": "Guest mode active", "user": user.to_dict()})

@bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})
