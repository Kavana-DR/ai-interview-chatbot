
from retriever import InterviewRetriever

retriever = InterviewRetriever()

tests = [
    ("Java inheritance", "What is inheritance in Java?"),
    ("Java ArrayList LinkedList", "What is the difference between ArrayList and LinkedList?"),
    ("Python list tuple", "What is the difference between a list and a tuple?"),
    ("Python decorators", "What is a Python decorator?"),
    ("RAG retrieval generation", "What is Retrieval-Augmented Generation?"),
    ("AI embeddings vectors", "What are embeddings?")
]

passed = 0

for query, expected_question in tests:
    results = retriever.search(query, top_k=1)
    actual = results[0]["question"] if results else None
    success = actual == expected_question
    passed += success

    print(f"\nQuery: {query}")
    print(f"Expected: {expected_question}")
    print(f"Retrieved: {actual}")
    print(f"Result: {'PASS' if success else 'FAIL'}")

print(f"\nTop-1 retrieval pass rate: {passed}/{len(tests)} "
      f"({passed / len(tests) * 100:.1f}%)")
