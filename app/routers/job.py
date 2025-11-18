from fastapi import APIRouter
from app.services.job_queue import create_job, get_result

import logging

router = APIRouter()

@router.post("/run")
def run(action: dict):
    logging.info("Received job request for script generation.")
    job_id = create_job(action)
    logging.info(f"Job {job_id} created and added to the queue.")
    return {"job_id": job_id}

@router.get("/job/{id}")
def job_status(id: str):
    logging.info(f"Status request received for job {id}.")
    result = get_result(id)
    if result:
        logging.info(f"Job {id} completed. Returning result.")
        return {"status": "completed", "result": result}
    else:
        logging.info(f"Job {id} is still in pending.")
        return {"status": "pending"}
