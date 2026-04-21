from flask import Blueprint, request, jsonify
from services.describe_service import generate_description

describe_bp = Blueprint("describe", __name__)


@describe_bp.post("/describe")
def describe():
    data = request.get_json(force=True)
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "text is required"}), 400

    if len(text) < 3:
        return jsonify({"error": "text is too short"}), 400

    result = generate_description(text)
    return jsonify(result)