import logging
from fastapi import FastAPI
from app.routers.config_gen import router as config_router

app = FastAPI()

app.include_router(config_router, prefix="/config", tags=["config"])

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

@app.get("/")
def welcom():
    return "Welcome to the Configuration Script Generator API!"

@app.get("/health")
def health_check():
    logging.info("Health check endpoint called.")
    return {"status": "ok"}