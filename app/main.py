# author : chenrensong@outlook.com

from fastapi import FastAPI, HTTPException
from InstructorEmbedding import INSTRUCTOR
import tiktoken
from typing import List
from pydantic import BaseModel
import logging
import os

# Constants
DEFAULT_INSTRUCTION = "Represent the query for retrieval"
DEFAULT_MODEL_NAME = 'text2vec-base-chinese'

# Models
class EmbeddingRequest(BaseModel):
    input: str
    model:str = DEFAULT_MODEL_NAME
    instruction: str = DEFAULT_INSTRUCTION

class EmbeddingUsage(BaseModel):
    prompt_tokens: int
    total_tokens: int

class EmbeddingData(BaseModel):
    embedding: List[float]
    index: int
    object: str = "embedding"

class EmbeddingResponse(BaseModel):
    data: List[EmbeddingData]
    model: str
    object: str = "list"
    usage: EmbeddingUsage

# FastAPI Application
app = FastAPI()
encoding = tiktoken.get_encoding("gpt2")
logging.basicConfig(level=logging.INFO)

@app.on_event("startup")
async def load_model():
    logging.info("Loading Instructor Embedding Model")
    models_path = "model/"
    model_dirs = [d for d in os.listdir(models_path) if os.path.isdir(os.path.join(models_path, d))]
    app.state.models = {}
    for model_dir in model_dirs:
        model_path = os.path.join(models_path, model_dir)
        app.state.models[model_dir] = INSTRUCTOR(model_path)
    logging.info("Instructor Embedding Model Loaded")

@app.get("/")
async def root():
    return {"Hello": "OpenAI Embedding"}

@app.post("/embeddings", response_model=EmbeddingResponse)
async def generate_embeddings(payload: EmbeddingRequest):
    if not payload.input:
        raise HTTPException(status_code=400, detail="Input text is required")

    if payload.model not in app.state.models:
        raise HTTPException(status_code=400, detail=f"Model {payload.model} not found")

    model = app.state.models[payload.model]
    embeddings = model.encode([payload.input, payload.instruction])

    tokens = encoding.encode(payload.input)
    prompt_tokens = len(tokens)
    response_tokens = len(embeddings[0])
    total_tokens = prompt_tokens + response_tokens

    data = [EmbeddingData(embedding=embeddings[0].tolist(), index=0)]
    usage = EmbeddingUsage(prompt_tokens=prompt_tokens, total_tokens=total_tokens)
    
    return {
        "data": data, 
        "model": payload.model, 
        "object": "list", 
        "usage": usage
    }
