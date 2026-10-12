
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

MODEL = "gemini-3.8-flash"


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    role = ""

    if request.method == "POST":
        role = request.form.get("role", "").strip()

        if not role:
            answer = "Please enter a job role."
        elif not client:
            answer = "API key missing. Check your .env file."
        else:
            try:
                response = client.models.generate_content(
                    model=MODEL,
                    contents=(
                        f"Generate 5 interview questions and concise sample "
                        f"answers for the role: {role}. Format them clearly."
                    )
                )
                answer = response.text or "No response received. Try again."

            except Exception:
                app.logger.exception("Gemini API request failed")
                answer = (
                    "AI request failed. Check the VS Code terminal for "
                    "the exact error."
                )

    return render_template("index.html", answer=answer, role=role)


if __name__ == "__main__":
    app.run(debug=True)
