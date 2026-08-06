""" 01 Добавление товаров

Создайте программу, которая подключается к MongoDB и:
- выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
- очищает коллекцию перед началом
- добавляет 3 товара с полями: name, price, stock
- выводит сообщение о количестве добавленных товаров
Пример вывода:
3 products inserted.
"""


from dataclasses import dataclass, asdict

from pymongo import MongoClient
from pymongo.collection import Collection

from local_settings_hw_43 import MONGODB_URL_WRITE


@dataclass
class Product:
    """Товар: name, price, stock"""
    name: str
    price: float
    stock: int

    def to_dict(self) -> dict:
        return asdict(self)


class MongoRepository:
    """Базовый репозиторий: инкапсулирует подключение к базе/коллекции MongoDB"""

    def __init__(self, client: MongoClient, db_name: str, collection_name: str):
        self._db = client[db_name]
        self._collection: Collection = self._db[collection_name]

    def clear(self) -> int:
        """Очищает коллекцию, возвращает количество удалённых документов"""
        result = self._collection.delete_many({})
        return result.deleted_count

    def find_all(self) -> list[dict]:
        return list(self._collection.find())


class ProductRepository(MongoRepository):
    """Репозиторий товаров — наследует общую логику работы с коллекцией
    и добавляет операции, специфичные для товаров"""

    def __init__(self, client: MongoClient):
        super().__init__(client, db_name="ich_edit",
                         collection_name="products_ich_edit")

    def add_products(self, products: list[Product]) -> int:
        """Добавляет список товаров, возвращает количество вставленных документов"""
        documents = [product.to_dict() for product in products]
        result = self._collection.insert_many(documents)
        return len(result.inserted_ids)

    def increase_prices(self, percent: float) -> int:
        """Увеличивает цену всех товаров на percent %,
        возвращает количество обновлённых документов"""
        multiplier = 1 + percent / 100
        result = self._collection.update_many({}, {"$mul": {"price": multiplier}})
        return result.modified_count


def main() -> None:
    products = [
        Product(name="Laptop", price=1200, stock=5),
        Product(name="Mouse", price=25, stock=50),
        Product(name="Keyboard", price=70, stock=20),
    ]

    with MongoClient(MONGODB_URL_WRITE) as client:
        repo = ProductRepository(client)
        repo.clear()
        inserted_count = repo.add_products(products)
        print(f"{inserted_count} products inserted.")


if __name__ == "__main__":
    main()
