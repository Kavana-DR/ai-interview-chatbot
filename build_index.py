
import json
import os
import joblib
import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

os.makedirs("data", exist_ok=True)

with open("data/interview_knowledge.json", "r", encoding="utf-8") as f:
    documents = json.load(f)

texts = [
    f"Role: {doc['role']}. Topic: {doc['topic']}. "
    f"Question: {doc['question']}. Answer: {doc['answer']}"
    for doc in documents
]

# Convert text into numerical vectors without downloading a model.
vectorizer = TfidfVectorizer(stop_words="english")
sparse_vectors = vectorizer.fit_transform(texts)

# FAISS works with dense numerical vectors.
vectors = sparse_vectors.toarray().astype("float32")
faiss.normalize_L2(vectors)

index = faiss.IndexFlatIP(vectors.shape[1])
index.add(vectors)

faiss.write_index(index, "data/interview.index")
joblib.dump(vectorizer, "data/tfidf_vectorizer.joblib")

with open("data/interview_metadata.json", "w", encoding="utf-8") as f:
    json.dump(documents, f, indent=2, ensure_ascii=False)

print(f"Success! Indexed {len(documents)} interview entries.")
print("Created FAISS index, vectorizer, and metadata.")
