from fastapi import FastAPI, Depends
from typing import Annotated
from db.database import session_maker
from db.models import Product, Order, StatusOrder
from pydantic import BaseModel
from sqlalchemy.orm import Load, joinedload
from controllers.products_router import router as products_router
from controllers.orders_router import router as orders_router
from controllers.testing_router import router as testing_router


app = FastAPI()

app.include_router(products_router)
app.include_router(orders_router)
app.include_router(testing_router)




