from flask import Flask, render_template, request
from model import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_msg = request.form.get("msg")
    if not user_msg:
        return "Please enter a message."
    response = get_bot_response(user_msg)
    return response

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
