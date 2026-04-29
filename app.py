from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "ESP32 Translator Server Running"

@app.route("/translate", methods=["POST"])
def translate():
    print("=== TRANSLATE HIT ===")
    print("BYTES RECEIVED:", len(request.data))

    return Response(bytes([128] * 4000), mimetype="application/octet-stream")