from decimal import Decimal
from typing import Annotated, Optional

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel, Field

engine = create_engine("sqlite:///:memory:", echo=True)

Session = sessionmaker(bind=engine)
session = Session()


class Base(DeclarativeBase):
    pass


# объявляю переиспользуемые типы через Annotated
str100 = Annotated[str, mapped_column(String(100))]
str255 = Annotated[str, mapped_column(String(255))]
price_type = Annotated[Decimal, mapped_column(Numeric(10, 2))]
intpk = Annotated[int, mapped_column(primary_key=True)]


# Задача 4
class Category(Base):
    __tablename__ = "categories"

    id: Mapped[intpk]
    name: Mapped[str100]
    description: Mapped[str255]

    products: Mapped[list["Product"]] = relationship(back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[intpk]
    name: Mapped[str100]
    price: Mapped[price_type]
    in_stock: Mapped[bool]

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    category: Mapped["Category"] = relationship(back_populates="products")


Base.metadata.create_all(engine)


class CategorySchema(BaseModel):
    name: str = Field(max_length=100)
    description: str = Field(max_length=255)


class ProductSchema(BaseModel):
    name: str = Field(max_length=100)
    price: Decimal = Field(gt=0)
    in_stock: bool
    category_id: Optional[int] = None
