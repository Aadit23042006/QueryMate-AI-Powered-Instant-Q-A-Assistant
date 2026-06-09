import os
from flask import Flask, request, jsonify, session, render_template
from google import genai

app = Flask(__name__)
app.secret_key = "any-random-string-here-to-enable-sessions"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/set-api-key", methods=["POST"])
def set_api_key():
    data = request.get_json()
    api_key = data.get("api_key")

    if not api_key:
        return jsonify({"success": False, "error": "No API key provided"}), 400

    session["gemini_api_key"] = api_key
    return jsonify({"success": True})

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message")
    api_key = session.get("gemini_api_key") or os.getenv("GEMINI_API_KEY")

    if not api_key:
        return jsonify({"success": False, "error": "Gemini API key not set. Please set it above."}), 400

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=user_message
        )

        return jsonify({"success": True, "message": response.text})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)