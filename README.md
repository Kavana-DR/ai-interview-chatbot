# AI Interview Preparation Assistant

An AI-powered interview preparation web application that generates role-specific interview questions and sample answers using Google's Gemini API and Retrieval-Augmented Generation (RAG).

## Features

- **AI-Generated Questions:** Generates interview questions and sample answers based on the selected job role.
- **Knowledge Retrieval:** Uses TF-IDF and FAISS to retrieve relevant information from a custom interview knowledge base.
- **Context-Aware Responses:** Supplies retrieved interview notes to Gemini to support relevant answer generation.
- **Source References:** Displays retrieved questions and topics used as context.
- **Retrieval Evaluation:** Includes a Python script to evaluate top-1 retrieval performance against reference questions.

## Tech Stack

- **Language:** Python
- **Backend:** Flask
- **AI API:** Google Gemini API
- **Retrieval:** TF-IDF, FAISS
- **Libraries:** scikit-learn, NumPy, Joblib
- **Frontend:** HTML, CSS, Bootstrap
- **Configuration:** python-dotenv

## Project Structure

```text
ai-interview-chatbot/
├── app.py
├── build_index.py
├── retriever.py
├── test_retriever.py
├── evaluate_retriever.py
├── requirements.txt
├── data/
│   └── interview_knowledge.json
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .env
└── .gitignore
```

Generated files such as the FAISS index, vectorizer, and metadata are created in the `data/` directory.

## Prerequisites

- Python 3.12
- A Google Gemini API key
- Internet access for API requests and package installation

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-interview-chatbot
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_api_key
```

Never commit your `.env` file or expose your API key.

### 5. Build the retrieval index

```bash
python build_index.py
```

This reads the interview knowledge base, creates TF-IDF vectors, and builds a FAISS index.

### 6. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Evaluation

Run the retrieval test:

```bash
python test_retriever.py
```

Evaluate top-1 retrieval against the reference questions:

```bash
python evaluate_retriever.py
```

The evaluation script reports the number and percentage of test queries for which the expected question is retrieved first. Results depend on the test queries and knowledge base.

## How It Works

1. Interview questions, topics, and answers are stored in a JSON knowledge base.
2. TF-IDF converts the stored text into numerical vectors.
3. FAISS searches for the most relevant entries for a user query.
4. Retrieved entries are added to the Gemini prompt as supporting context.
5. The application displays the generated interview questions and retrieved source references.

**Note:** This implementation uses keyword-based TF-IDF retrieval, not semantic embeddings. The knowledge base and evaluation set are currently small and can be expanded to improve coverage.

## Future Improvements

- Expand the interview knowledge base across more technical roles.
- Add difficulty-level selection.
- Improve retrieval using semantic embeddings.
- Expand answer-quality evaluation with a larger test set.
- Add automated tests and deploy the application.

## Security

Store API credentials in environment variables. Keep `.env`, virtual environments, and other secrets out of version control.

## License

This project is intended for learning and portfolio demonstration.