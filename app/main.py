#run command: python3 app/main.py

from flask import Flask, render_template, request, jsonify
from ai import translate_text


app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def hello_world():
    return render_template("index.html")


# @app.route("/translate", methods=["POST"])
# def translate():
#     text = request.form["text"]
#     translated_text = translate_text(text)
#     return render_template("index.html", translated_text=translated_text)


if __name__ == "__main__":
    app.run(debug=True, port=8000)


