from fastapi import APIRouter, Depends
from typing import Annotated
from db.database import session_maker
from db.models import Product, Order, StatusOrder


router = APIRouter(
    prefix="/orders",
    tags=["Orders API"],
)


# ORDER API
@router.get("/")
def get_orders(session: Annotated[dict, Depends(session_maker)]):
    orders = session.query(Order).all()
    session.close()
    return orders


@router.get("/{order_id:int}")
def get_order(order_id: int, session: Annotated[dict, Depends(session_maker)]):
    order = session.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        return {"status": "error", "message": "Order not found"}
    
    session.close()
    return order
