"""Insert the sample document chunks into a running pgvector database."""

import os

import psycopg

from rag_lab.data import DOCUMENTS
from rag_lab.store import rows_for_documents


def main() -> None:
    database_url = os.environ.get("DATABASE_URL", "postgresql://rag:rag@localhost:5432/rag")
    with psycopg.connect(database_url) as connection:
        with connection.cursor() as cursor:
            cursor.executemany(
                """
                INSERT INTO document_chunks (id, content, embedding)
                VALUES (%s, %s, %s::vector)
                ON CONFLICT (id) DO UPDATE
                SET content = EXCLUDED.content, embedding = EXCLUDED.embedding
                """,
                rows_for_documents(DOCUMENTS),
            )
        connection.commit()
    print(f"Seeded {len(DOCUMENTS)} document chunks.")


if __name__ == "__main__":
    main()
