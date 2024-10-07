from fastapi import FastAPI
from db.database import SessionLocal
from db.models import Product, Order, StatusOrder
from pydantic import BaseModel
from sqlalchemy.orm import Load, joinedload


app = FastAPI()
session = SessionLocal()


class ProductDTO(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


# TESTING
@app.get("/test")
def test_action():
    data = session.query(Order).first()
    return data


# ORDER API
@app.get("/orders")
def get_orders():
    orders = session.query(Order).all()
    return orders


@app.get("/orders/{order_id:int}")
def get_order(order_id: int):
    order = session.query(Order).filter(Order.id == order_id).first()
    
    if not order:
        return {"status": "error", "message": "Order not found"}
    
    return order


# PRODUCT API
@app.post("/products")
def create_product(product: ProductDTO):
    product = Product(
        name=product.name, 
        description=product.description, 
        price=product.price, 
        quantity=product.quantity
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return {"status": "success", "message": "Product created"}


@app.get("/products")
def get_products():
    products = session.query(Product).all()
    return products


@app.get("/products/{product_id:int}")
def get_product(product_id: int):
    product = session.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        return {"status": "error", "message": "Product not found"}
    
    return product


@app.put("/products/{product_id:int}")
def update_product(product_id: int, product_data: ProductDTO):
    product = session.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        return {"status": "error", "message": "Product not found"}
    
    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.quantity = product_data.quantity
    session.commit()
    return {"status": "success", "message": "Product updated"}


@app.delete("/products/{product_id:int}")
def delete_product(product_id: int):
    product = session.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        return {"status": "error", "message": "Product not found"}
    
    session.delete(product)
    session.commit()
    return {"status": "success", "message": "Product deleted"}
