from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import *
from .database import Base

#many to many 
category_products = Table('category_products_many', Base.metadata,
    Column('category_id', Integer, ForeignKey('categories.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name  = Column(String, index = True)

    products = relationship("Product",  secondary=category_products,  back_populates="categories")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index = True)
    categories = relationship("Category", secondary=category_products, back_populates="products")


