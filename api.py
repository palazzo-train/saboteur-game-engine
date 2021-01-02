import json
from fastapi import FastAPI
from mangum import Mangum


from engine.game_env.engine import GameEnv

app = FastAPI(title='Saboteur API',
              description='API to interact with Saboteur Engine')
# app.include_router(router, prefix="/v1")


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

# to make it work with Amazon Lambda, we create a handler object
handler = Mangum(app=app)
