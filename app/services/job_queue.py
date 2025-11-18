import json
from app.core.config import redis_client

def create_job(payload: dict) -> str:
    job_id = redis_client.incr("job_id_counter")

    # serialize payload values to JSON strings
    payload_serialized = {k: json.dumps(v) for k, v in payload.items()}
    redis_client.hset(f"job:{job_id}", mapping=payload_serialized)
    redis_client.lpush("job_queue", job_id)

    return str(job_id)


def get_result(job_id: str) -> dict:
    result_serialized = redis_client.hgetall(f"job_result:{job_id}")

    if not result_serialized:
        return {} 
    result = {}
    for k, v in result_serialized.items():
        try:
            result[k.decode()] = json.loads(v.decode())
        except json.JSONDecodeError:
            result[k.decode()] = v.decode()
    return result
