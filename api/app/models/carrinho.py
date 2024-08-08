from typing import  Optional
from sqlmodel import Field, SQLModel
from datetime import date


class CarrinhoBase(SQLModel):
    idproduto: int
    datacarrinho: date
    # quantidade:int


class Carrinho(CarrinhoBase, table=True):
    __tablename__: str = 'carrinhos'  
    __table_args__ = {'schema': 'dbfiafastapi'}
    id: int = Field(default=None, primary_key=True)

class CarrinhoRequest(CarrinhoBase):
  pass

class CarrinhoResponse(SQLModel):
  id: int
  idproduto:int
  datacarrinho:date
 

