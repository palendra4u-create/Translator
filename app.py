from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "ESP32 Translator Server Running"

@app.route("/translate", methods=["POST"])
def translate():
    print("HEADERS:", dict(request.headers))
    print("DATA LENGTH:", len(request.data))

    if len(request.data) == 0:
        return jsonify({"error": "No audio data"}), 400

    with open("last_audio.raw", "wb") as f:
        f.write(request.data)

    return send_file("demo_response.mp3", mimetype="audio/mpeg")