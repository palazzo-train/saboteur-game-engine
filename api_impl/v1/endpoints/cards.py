from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def get_cards_hello():
    return  { 'cards' : 'hello'}
