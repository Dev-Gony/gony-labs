$ErrorActionPreference = 'Stop'

python -m pytest `
  01-daily-interview-gym/tests `
  02-fastapi-lab/tests `
  03-postgresql-lab/tests `
  04-docker-lab/tests `
  05-redis-queue-lab/tests `
  06-api-reliability-lab/tests `
  07-mini-rag/tests `
  08-mcp-tool-lab/tests `
  -q
