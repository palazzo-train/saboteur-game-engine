from fastapi import APIRouter
from .endpoints import cards , game_state

router = APIRouter()
router.include_router(cards.router, prefix="/cards", tags=["Cards"])
router.include_router(game_state.router, prefix="/game-state", tags=["Game State"])
