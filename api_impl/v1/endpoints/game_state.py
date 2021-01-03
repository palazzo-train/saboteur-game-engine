import json
from fastapi import APIRouter
from engine.game_env.engine import GameEnv

router = APIRouter()


@router.get("/init")
async def get_init():
    g_env = GameEnv()
    g_env.init()

    m = g_env.map
    m_json = json.dumps(m.tolist())

    return {"game map": m_json }