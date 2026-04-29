from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "ESP32 Translator Server Running"

@app.route("/translate", methods=["POST"])
def translate():
    try:
        raw_audio = request.data
        direction = request.headers.get("X-Direction", "hi-en")

        print("Direction:", direction)
        print("Bytes Received:", len(raw_audio))

        if len(raw_audio) == 0:
            return jsonify({"error": "No audio data"}), 400

        with open("last_audio.raw", "wb") as f:
            f.write(raw_audio)

        mp3_path = "demo_response.mp3"

        if not os.path.exists(mp3_path):
            return jsonify({"error": "demo_response.mp3 missing"}), 500

        return send_file(
            mp3_path,
            mimetype="audio/mpeg"
        )

    except Exception as e:
        print("SERVER ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)