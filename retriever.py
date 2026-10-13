
import json
import joblib
import faiss
import numpy as np

INDEX_PATH = "data/interview.index"
VECTOR_PATH = "data/tfidf_vectorizer.joblib"
METADATA_PATH = "data/interview_metadata.json"


class InterviewRetriever:
    def __init__(self):
        self.index = faiss.read_index(INDEX_PATH)
        self.vectorizer = joblib.load(VECTOR_PATH)

        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            self.documents = json.load(f)

    def search(self, query, top_k=3):
        query_vector = self.vectorizer.transform([query])
        query_vector = query_vector.toarray().astype("float32")
        faiss.normalize_L2(query_vector)

        scores, indices = self.index.search(query_vector, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx >= 0 and score > 0:
                results.append({
                    "score": float(score),
                    **self.documents[idx]
                })

        return results
