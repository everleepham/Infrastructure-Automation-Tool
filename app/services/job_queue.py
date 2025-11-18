from app.core.config import redis_client

def create_job(payload: dict) -> str:
    job_id = redis_client.incr("job_id_counter")
    redis_client.hset(f"job:{job_id}", mapping=payload)
    redis_client.lpush("job_queue", job_id)
    return str(job_id)

def get_result(job_id: str) -> dict:
    result = redis_client.hgetall(f"job_result:{job_id}")
    return {k.decode(): v.decode() for k, v in result.items()} if result else {}