from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/hello')
async def get_hello_world(name: str = "world"):
    return {'hello': name}

@app.get('/hello/{name}')
async def get_hello_name(name: str):
    return {'hello': name}

@app.post('/hello')
async def post_hello_name(data: dict):
    return {'hello': data.get('name', 'world')}