from fastapi import APIRouter
from app.services.generator import generate_script

import logging


router = APIRouter()

@router.post("/generate")
def generate(config: dict):
    logging.info("Received configuration for script generation.")
    script = generate_script(config)
    logging.info("Script generation completed.")
    return {"script": script}