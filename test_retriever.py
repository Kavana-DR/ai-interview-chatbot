
from retriever import InterviewRetriever

retriever = InterviewRetriever()

queries = [
    "Java inheritance",
    "Python list and tuple",
    "AI engineer embeddings"
]

for query in queries:
    print(f"\nQuery: {query}")
    results = retriever.search(query, top_k=3)

    for result in results:
        print(f"- {result['role']} | {result['topic']}")
        print(f"  Question: {result['question']}")
        print(f"  Score: {result['score']:.3f}")
