from flask import Blueprint, request, jsonify, Response
from app.services.document_service import generate_document, generate_diagram_svg

bp = Blueprint("documents", __name__, url_prefix="/documents")

@bp.route("/generate", methods=["POST"])
def generate_doc():
    data = request.get_json() or {}
    doc_type = data.get("type", "report")
    title = data.get("title", "Project Summary")
    content = data.get("content", "")

    if doc_type == "diagram":
        svg = generate_diagram_svg(title)
        return Response(svg, mimetype="image/svg+xml")

    report = generate_document(title, content)
    return jsonify({"type": doc_type, "title": title, "content": report})
