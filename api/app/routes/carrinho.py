from fastapi import HTTPException, status, APIRouter
from typing import Any, List
from app.models.carrinho import Carrinho, CarrinhoResponse, CarrinhoRequest
from sqlmodel import select, Session
from app.db import ActiveSession
from app.kafka_producer import produce_message
import json
from datetime import date

router = APIRouter()


def custom_json_serializer(obj):
    """Converte objetos de data para strings no formato ISO."""
    if isinstance(obj, (date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


@router.post("/carrinhos", response_model=CarrinhoResponse, status_code=status.HTTP_201_CREATED)
# async def Inserir_Aluno(aluno: str):
async def Inserir_Carrinho(carrinho: CarrinhoRequest, session: Session = ActiveSession)-> Any:
  db_carrinho = Carrinho.from_orm(carrinho)
  session.add(db_carrinho)
  await session.commit()
  await session.refresh(db_carrinho)

  # Converter datacarrinho para string no formato ISO
  carrinho_dict = db_carrinho.dict()  
  message = json.dumps(carrinho_dict, default=custom_json_serializer)
  
  # Produzir mensagem Kafka
 
  produce_message('carrinho', message)
  
  return db_carrinho
