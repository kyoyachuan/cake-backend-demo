from pydantic import BaseModel
from typing import List, Optional


class RegisterForm(BaseModel):
    username: str
    email: str
    password: str


class ProductToCarts(BaseModel):
    id: int
    quantity: Optional[int] = 1


class Card(BaseModel):
    name: str
    front: str
    back: str


class CartsUpdateQuantity(BaseModel):
    id: int
    quantity: int


class Carts(BaseModel):
    id: int


class CartsToOrders(BaseModel):
    ids: List[int]
