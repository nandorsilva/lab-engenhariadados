from fastapi import HTTPException, status, APIRouter
from typing import Any, List
from app.models.carrinho import Carrinho, CarrinhoResponse, CarrinhoRequest
from sqlmodel import select, Session
from app.db import ActiveSession

router = APIRouter()


       

@router.post("/carrinhos", response_model=CarrinhoResponse, status_code=status.HTTP_201_CREATED)
# async def Inserir_Aluno(aluno: str):
async def Inserir_Carrinho(aluno: CarrinhoRequest, session: Session = ActiveSession)-> Any:
  db_carrinho = Carrinho.from_orm(aluno)
  session.add(db_carrinho)
  await session.commit()
  await session.refresh(db_carrinho)
  return db_carrinho
