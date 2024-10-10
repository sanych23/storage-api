from fastapi import APIRouter, Depends
from typing import Annotated
from db.database import session_maker
from db.models import Product, Order, StatusOrder
from serializers.OrderResultDTO import OrderResDTO, ProductOrderCreateDTO
from typing import List
from sqlalchemy.orm import joinedload
from db.models import OrderItem
from datetime import datetime


router = APIRouter(
    prefix="/orders",
    tags=["Orders API"],
)


# ORDER API
@router.get("/")
def get_orders(session: Annotated[dict, Depends(session_maker)]) -> List[OrderResDTO]:
    orders = session.query(Order).options(
        joinedload(Order.status),
        joinedload(Order.orderitems).joinedload(OrderItem.products)
    ).all()
    session.close()
    return orders


@router.get("/{order_id:int}")
def get_order(order_id: int, session: Annotated[dict, Depends(session_maker)]) -> OrderResDTO:
    order = session.query(Order).options(
        joinedload(Order.status),
        joinedload(Order.orderitems).joinedload(OrderItem.products)
    ).filter(Order.id == order_id).first()
    
    if not order:
        return {"status": "error", "message": "Order not found"}
    
    session.close()
    return order


@router.patch("/{order_id:int}/{status_id:int}")
def update_order_status(order_id: int, status_id: int, session: Annotated[dict, Depends(session_maker)]):
    order = session.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        return {"status": "error", "message": "Order not found"}
    
    order.status_id = status_id
    session.commit()
    
    session.close()
    return {"status": "success", "message": "Order status updated"}


@router.post("/")
def create_order(products: List[ProductOrderCreateDTO], session: Annotated[dict, Depends(session_maker)]):
    for product in products:
        product_storage = session.query(Product).filter(Product.id == product.product_id).first()
        if not product_storage:
            return {"status": "error", "message": "Product not found"}
        if product.quantity > product_storage.quantity:
            return {"status": "error", "message": f"Insufficient quantity {product_storage.name}"}
    
    order = Order(
        status_id=1,
        created_at=datetime.now(),
    )
    session.add(order)
    session.commit()
    session.refresh(order)
    
    for product in products:
        product_storage = session.query(Product).filter(Product.id == product.product_id).first()
        product_storage.quantity -= product.quantity
        order_item = OrderItem(
            order_id=order.id,
            product_id=product.product_id,
            quantity=product.quantity
        )
        session.add(order_item)
        session.commit()
        session.refresh(order_item)
    
    return {"status": "success", "message": "Order created"}