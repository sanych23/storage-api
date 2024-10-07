from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base


# Product (id, name, description, price, quantity)
# Order (id, created_at, status)
# OrderItem (id, order_id, product_id, quantity)
Base = declarative_base()


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    quantity = Column(Integer, nullable=False)


class StatusOrder(Base):
    __tablename__ = "status-order"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    status = Column(Integer, ForeignKey("status-order.id"), nullable=False)


class OrderItem(Base):
    __tablename__ = "order-item"

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    quantity = Column(Integer, nullable=False)
