#run command: python3 app/main.py


from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)


