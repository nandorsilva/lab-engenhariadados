from typing import  Optional
from sqlmodel import Field, SQLModel
from datetime import date


class CarrinhoBase(SQLModel):
    idProduto: int
    dataCarrinho: date
    quantidade:int


class Carrinho(CarrinhoBase, table=True):
    __tablename__: str = 'carrinhos'  
    id: int = Field(default=None, primary_key=True)

class CarrinhoRequest(CarrinhoBase):
  pass

class CarrinhoResponse(SQLModel):
  id: int
  idProduto:int
 

