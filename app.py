from flask import Flask, request, send_file, jsonify
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "ESP32 Translator Server Running"

@app.route("/translate", methods=["POST"])
def translate():
    direction = request.headers.get("X-Direction", "hi-en")
    raw_audio = request.data

    if not raw_audio:
        return jsonify({"error": "No audio data"}), 400

    with open("last_audio.raw", "wb") as f:
        f.write(raw_audio)

    return send_file("demo_response.mp3", mimetype="audio/mpeg")