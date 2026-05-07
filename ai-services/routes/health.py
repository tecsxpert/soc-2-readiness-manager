from flask import Blueprint, jsonify
from services.chroma_client import get_collection
from services.cache_service import get_cache_stats
import time

START_TIME = time.time()

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health_check():
    uptime_seconds = int(time.time() - START_TIME)

    # Check ChromaDB status
    try:
        collection = get_collection()
        chroma_count = collection.count()
        chroma_status = "ok"
    except Exception:
        chroma_count = 0
        chroma_status = "error"

    # Check Redis cache status
    cache_stats = get_cache_stats()

    return jsonify({
        "status": "ok",
        "uptime_seconds": uptime_seconds,
        "model": "llama-3.3-70b-versatile",
        "chroma_status": chroma_status,
        "chroma_chunks": chroma_count,
        "cache": cache_stats,
        "service": "ai-service",
        "version": "1.0.0"
    })