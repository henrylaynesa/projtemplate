from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def hello():
    return jsonify({"message": "Hello from Flask!"})


@main_bp.route("/health")
def health():
    return jsonify({"status": "healthy"})
