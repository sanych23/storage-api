from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Table
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.ext.declarative import declarative_base


# Product (id, name, description, price, quantity)
# Order (id, created_at, status)
# OrderItem (id, order_id, product_id, quantity)
Base = declarative_base()


class StatusOrder(Base):
    __tablename__ = "status-order"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    orders = relationship("Order", back_populates="status")


class OrderItem(Base):
    __tablename__ = "orderitem"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    products = relationship('Product', back_populates="orderitems")

    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    orderitems = relationship("Order", back_populates="orderitems")
    
    quantity = Column(Integer, nullable=False)


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    quantity = Column(Integer, nullable=False)
    orderitems = relationship("OrderItem", back_populates="products")


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    status_id = Column(Integer, ForeignKey("status-order.id"), nullable=False)
    status = relationship("StatusOrder", back_populates="orders")
    orderitems = relationship("OrderItem", back_populates="orderitems")
    









# WORK VARIANT
# class StatusOrder(Base):
#     __tablename__ = "status-order"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     orders = relationship("Order", back_populates="status")


# class OrderItem(Base):
#     __tablename__ = "orderitem"
#     id = Column(Integer, primary_key=True)
#     product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
#     order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
#     quantity = Column(Integer, nullable=False)


# class Product(Base):
#     __tablename__ = "product"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     description = Column(String, nullable=False)
#     price = Column(Float, nullable=False, default=0.0)
#     quantity = Column(Integer, nullable=False)
#     orders = relationship("Order", secondary='orderitem', back_populates="products")


# class Order(Base):
#     __tablename__ = "order"

#     id = Column(Integer, primary_key=True)
#     created_at = Column(DateTime, nullable=False)
#     status_id = Column(Integer, ForeignKey("status-order.id"), nullable=False)
#     status = relationship("StatusOrder", back_populates="orders", lazy="joined")
#     products = relationship("Product", secondary='orderitem', back_populates="orders", lazy="joined")
    
