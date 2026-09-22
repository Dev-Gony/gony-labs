import os
from typing import Any

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from redis import Redis
from redis.exceptions import RedisError
from rq import Queue
from rq.job import Job

from .jobs import simulated_long_task


app = FastAPI(title="Redis Queue Lab")


class JobCreate(BaseModel):
    seconds: int = Field(default=10, ge=1, le=30)


def get_queue() -> Queue:
    return Queue(connection=Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379/0")))


def job_payload(job: Job) -> dict[str, Any]:
    return {"id": job.id, "status": job.get_status(), "result": job.result}


@app.get("/health")
def health() -> dict[str, str]:
    try:
        get_queue().connection.ping()
    except RedisError as exc:
        raise HTTPException(status_code=503, detail="Redis unavailable") from exc
    return {"status": "ok"}


@app.post("/jobs", status_code=status.HTTP_202_ACCEPTED)
def create_job(payload: JobCreate) -> dict[str, str]:
    job = get_queue().enqueue(simulated_long_task, payload.seconds, job_timeout=60, result_ttl=3600)
    return {"id": job.id, "status": job.get_status()}


@app.get("/jobs/{job_id}")
def get_job(job_id: str) -> dict[str, Any]:
    try:
        job = Job.fetch(job_id, connection=get_queue().connection)
    except Exception as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    return job_payload(job)
