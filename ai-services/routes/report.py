from flask import Blueprint, request, jsonify
from services.report_service import generate_report

report_bp = Blueprint("report", __name__)


@report_bp.post("/generate-report")
def create_report():
    # Step 1 - Get JSON data
    data = request.get_json(force=True)

    # Step 2 - Validate input exists
    if not data:
        return jsonify({
            "error": "Request body is required",
            "status": "failed"
        }), 400

    text = data.get("text", "").strip()

    # Step 3 - Validate text field
    if not text:
        return jsonify({
            "error": "text field is required",
            "status": "failed"
        }), 400

    # Step 4 - Validate minimum length
    if len(text) < 3:
        return jsonify({
            "error": "text must be at least 3 characters",
            "status": "failed"
        }), 400

    # Step 5 - Validate maximum length
    if len(text) > 500:
        return jsonify({
            "error": "text must not exceed 500 characters",
            "status": "failed"
        }), 400

    # Step 6 - Generate report and return
    result = generate_report(text)
    return jsonify(result)