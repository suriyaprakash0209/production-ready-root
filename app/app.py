from flask import Flask, jsonify
from logger import setup_logger
import config

app = Flask(__name__)

# Initialize logger
logger = setup_logger()

@app.route("/")
def home():
    logger.info("Home endpoint accessed")
    return jsonify({
        "message": "Hii there this is suriya Flask CI/CD App is running 🚀"
    })

@app.route("/health")
def health():   # ✅ FIXED (added :)
    logger.info("Health check endpoint accessed")
    return jsonify({
        "status": "healthy",
        "service": "flask-app"
    }), 200

@app.route("/version")
def version():
    logger.info("Version endpoint accessed")
    return jsonify({
        "version": config.APP_VERSION
    })

if __name__ == "__main__":
    logger.info("Starting Flask application")
    app.run(host="0.0.0.0", port=5000)