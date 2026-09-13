from decimal import Decimal
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from pydantic import BaseModel, Field

engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2))
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")


Base.metadata.create_all(engine)


class CategorySchema(BaseModel):
    name: str = Field(max_length=100)
    description: str = Field(max_length=255)


class ProductSchema(BaseModel):
    name: str = Field(max_length=100)
    price: Decimal = Field(gt=0)
    in_stock: bool
    category_id: Optional[int] = None



