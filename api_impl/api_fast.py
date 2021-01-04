import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .v1.routers import router


from engine.game_env.engine import GameEnv

app = FastAPI(title='Saboteur API',
              description='API to interact with Saboteur Engine')
app.include_router(router, prefix="/v1")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "from FastAPI & API Gateway"}



@app.get("/hello")
def read_root_2():
    return {"XX  Hello Reader": "from HHHSDF FastAPI & API Gateway"}

@app.get("/init")
def read_init():
    g_env = GameEnv()
    g_env.init()

    m = g_env.map
    m_json = json.dumps(m.tolist())

    return {"game map": m_json }
