from flask import Flask, request
import logging  

logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
from middleware.security_middleware import security_middleware

# Step 1: Create app FIRST
app = Flask(__name__)

# Step 2: Then use it
@app.before_request
def before_request():
    return security_middleware()

# Sample route
@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

# Run app
if __name__ == "__main__":
    app.run(debug=True)

from flask import request

@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    return {
        "message": "Request passed middleware",
        "data": data
    }

from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from middleware.security_middleware import security_middleware

app = Flask(__name__)

# Initialize Rate Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"]  # GLOBAL LIMIT
)

# Middleware (Day 3)
@app.before_request
def before_request():
    return security_middleware()

# Test route
@app.route("/test", methods=["POST"])
def test():
    data = request.get_json()
    return {
        "message": "Request passed middleware",
        "data": data
    }

# Heavy endpoint (STRICT LIMIT)
@app.route("/generate-report", methods=["POST"])
@limiter.limit("10 per minute")  # SPECIAL LIMIT
def generate_report():
    return {
        "message": "Report generated successfully"
    }

# Health check
@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def home():
    return "Server is working"


