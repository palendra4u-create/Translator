from flask import Flask, request, send_file, jsonify
import os
import tempfile

app = Flask(__name__)

@app.route("/")
def home():
    return "ESP32 Translator Server Running"

@app.route("/translate", methods=["POST"])
def translate_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio uploaded"}), 400

    audio = request.files["audio"]
    direction = request.form.get("direction", "hi-en")

    temp_in = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio.save(temp_in.name)

    # TODO:
    # 1. Speech-to-Text
    # 2. Translate based on direction
    # 3. Text-to-Speech generate output.wav/mp3

    # Demo placeholder response:
    demo_path = "demo_response.mp3"

    if not os.path.exists(demo_path):
        return jsonify({"error": "No demo_response.mp3 found"}), 500

    return send_file(demo_path, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)