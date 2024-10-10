from pydantic import BaseModel
from db.models import Order, StatusOrder, Product
from datetime import datetime
from typing import List


class ProductOrderCreateDTO(BaseModel):
    product_id: int
    quantity: int


class StatusOrderDTO(BaseModel):
    id: int
    name: str    


class ProductOrderDTO(BaseModel):
    id: int
    name: str
    description: str
    price: int


class OrderItemsDTO(BaseModel):
    quantity: int
    products: ProductOrderDTO


class OrderResDTO(BaseModel):
    id: int
    created_at: datetime
    status: StatusOrderDTO
    orderitems: List[OrderItemsDTO]
