from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from db.database import session_maker
from db.models import Product
from serializers.ProductDTO import ProductDTO


router = APIRouter(
    prefix="/products",
    tags=["Products API"],
)

# PRODUCT API
@router.post("/")
def create_product(product: ProductDTO, session: Annotated[dict, Depends(session_maker)]):
    product = Product(
        name=product.name, 
        description=product.description, 
        price=product.price, 
        quantity=product.quantity
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close()
    return {"status": "success", "message": "Product created"}


@router.get("/")
def get_products(session: Annotated[dict, Depends(session_maker)]):
    products = session.query(Product).all()
    session.close()
    return products


@router.get("/{product_id:int}")
def get_product(product_id: int, session: Annotated[dict, Depends(session_maker)]):
    product = session.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        return {"status": "error", "message": "Product not found"}
    
    session.close()
    return product


@router.put("/{product_id:int}")
def update_product(product_id: int, product_data: ProductDTO, session: Annotated[dict, Depends(session_maker)]):
    product = session.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        return {"status": "error", "message": "Product not found"}
    
    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.quantity = product_data.quantity
    session.commit()
    
    session.close()
    return {"status": "success", "message": "Product updated"}


@router.delete("/{product_id:int}")
def delete_product(product_id: int, session: Annotated[dict, Depends(session_maker)]):
    product = session.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        return {"status": "error", "message": "Product not found"}
    
    session.delete(product)
    session.commit()

    session.close()
    return {"status": "success", "message": "Product deleted"}


