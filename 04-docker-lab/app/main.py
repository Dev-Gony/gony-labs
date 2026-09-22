import os

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text


app = FastAPI(title="Docker Lab")
database_url = os.environ.get("DATABASE_URL", "postgresql+psycopg://toy_user:change-me-locally@db:5432/toy_labs")
engine = create_engine(database_url, pool_pre_ping=True)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/db-health")
def db_health() -> dict[str, str]:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Database unavailable") from exc
    return {"status": "ok"}
