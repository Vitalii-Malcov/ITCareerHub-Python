from decimal import Decimal
from typing import Optional
from sqlalchemy import create_engine, ForeignKey, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from pydantic import BaseModel, Field

engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255))
    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    in_stock: Mapped[bool] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products")


Base.metadata.create_all(engine)


class CategorySchema(BaseModel):
    name: str = Field(max_length=100)
    description: str = Field(max_length=255)


class ProductSchema(BaseModel):
    name: str = Field(max_length=100)
    price: Decimal = Field(gt=0)  # цена должна быть больше нуля
    in_stock: bool
    # категория не обязательна, поэтому используем Optional
    category_id: Optional[int] = None
