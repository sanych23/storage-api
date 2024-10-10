from fastapi import APIRouter, Depends
from typing import Annotated
from db.database import session_maker
from db.models import Product, Order, StatusOrder, OrderItem
from sqlalchemy.orm import joinedload
from sqlalchemy import select
from dto.OrderResultDTO import OrderResDTO
from typing import List

router = APIRouter(
    prefix="/testing",
    tags=["Testing API"],
)


# TESTING
@router.get("/test_1")
def test_action(session: Annotated[dict, Depends(session_maker)])->List[OrderResDTO]:
    
    data = session.query(Order).options(
        joinedload(Order.status),
        joinedload(Order.orderitems).joinedload(OrderItem.products)
    ).all()
    # data.products()
    # print(session)
    session.close()
    return data

