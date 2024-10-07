from fastapi import FastAPI
from db.database import SessionLocal
from db.models import Product

app = FastAPI()
session = SessionLocal()




