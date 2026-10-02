from flask import Blueprint, request, jsonify
from app.services.ai_service import generate_ai_reply
from app.models import Session, Message, User, db
from flask_login import current_user, login_required
import json

bp = Blueprint("chat", __name__, url_prefix="/chat")

@bp.route("/send", methods=["POST"])
@login_required
def send_chat():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    session = Session.query.filter_by(user_id=current_user.id).order_by(Session.created_at.desc()).first()
    if not session:
        session = Session(title=prompt[:50], user_id=current_user.id)
        db.session.add(session)
        db.session.commit()

    user_message = Message(session_id=session.id, role="user", content=prompt)
    db.session.add(user_message)
    db.session.commit()

    reply = generate_ai_reply(prompt)

    assistant_message = Message(session_id=session.id, role="assistant", content=reply)
    db.session.add(assistant_message)
    db.session.commit()

    return jsonify({"reply": reply, "session_id": session.id})

@bp.route("/history", methods=["GET"])
@login_required
def history():
    sessions = Session.query.filter_by(user_id=current_user.id).order_by(Session.created_at.desc()).all()
    result = []
    for session in sessions:
        result.append({
            "id": session.id,
            "title": session.title,
            "created_at": session.created_at.isoformat(),
            "messages": [m.to_dict() for m in session.messages]
        })
    return jsonify(result)
