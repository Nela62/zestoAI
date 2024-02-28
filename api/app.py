from fastapi import FastAPI, HTTPException, Request

import logging

import config


log = logging.getLogger(__name__)

app = FastAPI(
    title="Simplifying HR Compliance API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/docs/openapi.json",
)
app.router.prefix = "/api"

# open_ai_key = config.open_ai_key()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/prompt")
def get_ai_response(prompt: str):

    return {"response": "AI's response"}


@app.get("/db/store")
def store_data():
    return {"response": "Data stored"}
