CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE document_chunks (
  id TEXT PRIMARY KEY,
  content TEXT NOT NULL,
  embedding vector(256) NOT NULL
);
CREATE INDEX document_chunks_embedding_idx
  ON document_chunks USING hnsw (embedding vector_cosine_ops);
