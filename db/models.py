from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, mapped_column, Mapped
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
    # order_items = relationship("OrderItem", backref="products")


class StatusOrder(Base):
    __tablename__ = "status-order"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    orders = relationship("Order", back_populates="status")


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    status_id = Column(Integer, ForeignKey("status-order.id"), nullable=False)
    status = relationship("StatusOrder", back_populates="orders", lazy="joined")
    # products = relationship(back_populates="orders", secondary="order-item")


# class OrderItem(Base):
    # __tablename__ = "order-item"

    # id = Column(Integer, primary_key=True)
    
    # order_id = Column(Integer, ForeignKey("order.id"))
    # product_id = Column(Integer, ForeignKey("product.id"))

    # order_id = mapped_column(ForeignKey("order.id"), primary_key=True)
    # product_id = mapped_column(ForeignKey("product.id"), primary_key=True)
    # quantity = Column(Integer, nullable=False)
