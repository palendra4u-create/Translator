from flask import Flask, Response, request
import math

app = Flask(__name__)

@app.route("/")
def home():
    return "ESP32 Translator Server Running"

@app.route("/translate", methods=["POST"])
def translate():
    samples = bytearray()

    for i in range(8000):
        val = int((math.sin(i * 0.05) + 1) * 127)
        samples.append(val)

    return Response(samples, mimetype="application/octet-stream")