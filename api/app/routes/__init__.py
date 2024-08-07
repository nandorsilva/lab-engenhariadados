from fastapi import APIRouter

from .carrinho import router as carrinho_router

main_router = APIRouter()

main_router.include_router(carrinho_router, prefix="/carrinho", tags=["carrinho"])

