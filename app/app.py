#run command: python3 app/main.py

from flask import Flask, render_template, request, jsonify
from .translator import translate_text
from flask_cors import CORS


app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
async def translate():
    data = request.json
    text = data.get("text")
    target_language = data.get("targetLanguage")


    translated_text = await translate_text(text, target_language)
    return jsonify({"reply": translated_text})


if __name__ == "__main__":
    app.run(debug=True, port=8080)


