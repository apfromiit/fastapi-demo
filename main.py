from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class DataModel(BaseModel):
    name: str = "world"

@app.get('/hello')
async def get_hello_world(name: str = "world"):
    return {'hello': name}

@app.get('/hello/{name}')
async def get_hello_name(name: str):
    return {'hello': name}

@app.post('/hello')
async def post_hello_name(data: DataModel):
    return {'hello': data.name}