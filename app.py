
import os

from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai

from retriever import InterviewRetriever

load_dotenv()

app = Flask(__name__)

# Gemini API configuration
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None
MODEL = "gemini-3.8-flash"

# Load the retrieval system once at startup
retriever = InterviewRetriever()


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    role = ""

    if request.method == "POST":
        role = request.form.get("role", "").strip()

        if not role:
            answer = "Please enter a job role."

        elif not client:
            answer = "Gemini API key missing. Check your .env file."

        else:
            try:
                # Retrieve relevant interview knowledge
                documents = retriever.search(role, top_k=3)

                if not documents:
                    answer = (
                        "No relevant interview notes found. "
                        "Try Java Developer, Python Developer, "
                        "or AI Software Engineer."
                    )

                else:
                    context = "\n\n".join(
                        f"Role: {doc['role']}\n"
                        f"Topic: {doc['topic']}\n"
                        f"Question: {doc['question']}\n"
                        f"Answer: {doc['answer']}"
                        for doc in documents
                    )

                    # Generate an answer grounded in retrieved notes
                    response = client.models.generate_content(
                        model=MODEL,
                        contents=(
                            "You are an AI interview preparation assistant.\n"
                            "Use the retrieved notes as supporting context. "
                            "You may add general knowledge where necessary, "
                            "but do not invent sources or claim unsupported "
                            "facts came from the notes.\n\n"
                            f"Retrieved interview notes:\n{context}\n\n"
                            f"Generate 5 useful interview questions with "
                            f"concise sample answers for: {role}."
                        )
                    )

                    answer = (
                        response.text
                        or "No response received. Please try again."
                    )

                    # Show retrieved source questions
                    sources = "\n".join(
                        f"- {doc['topic']}: {doc['question']}"
                        for doc in documents
                    )

                    answer += "\n\nSources retrieved:\n" + sources

            except Exception:
                app.logger.exception("Interview chatbot request failed")
                answer = (
                    "Sorry, the request failed. Check the VS Code "
                    "terminal for details and verify your API configuration."
                )

    return render_template(
        "index.html",
        answer=answer,
        role=role
    )


if __name__ == "__main__":
    app.run(debug=True)
