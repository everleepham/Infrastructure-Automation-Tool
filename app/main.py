import logging
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def welcom():
    return "Welcome to the Configuration Script Generator API!"

@app.get("/health")
def health_check():
    logging.info("Health check endpoint called.")
    return {"status": "ok"}