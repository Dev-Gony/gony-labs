import argparse

from rag_lab.data import DOCUMENTS
from rag_lab.retrieval import answer_from_context, retrieve


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a local Mini RAG retrieval.")
    parser.add_argument("question")
    args = parser.parse_args()
    results = retrieve(args.question, DOCUMENTS)
    for rank, document in enumerate(results, start=1):
        print(f"{rank}. [{document.id}] {document.content}")
    print()
    print(answer_from_context(args.question, results))


if __name__ == "__main__":
    main()
