from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # связь "один ко многим": одна категория — много продуктов
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey("categories.id"))  # внешний ключ

    category = relationship("Category", back_populates="products")


engine = create_engine("sqlite:///shop.db")
Base.metadata.create_all(engine)  # создаёт таблицы, если их ещё нет

Session = sessionmaker(bind=engine)
session = Session()

def get_or_create_category(name, description):
    category = session.query(Category).filter_by(name=name).first()
    if category is None:
        category = Category(name=name, description=description)
        session.add(category)
        session.commit()
    return category


def get_or_create_product(name, price, in_stock, category):
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")

    product = session.query(Product).filter_by(name=name).first()
    if product is None:
        product = Product(name=name, price=price, in_stock=in_stock, category=category)
        session.add(product)
        session.commit()
    return product
