""" 02. Увеличение цен

Продолжите предыдущую задачу. Теперь программа должна:
- увеличить цену всех товаров на 20%
- вывести количество обновлённых записей
- затем вывести список всех товаров с новыми ценами

Пример вывода:
Prices updated for 3 products.

Updated products:
- Pen — $1.80
- Notebook — $4.79
- Backpack — $30.00"""

from pymongo import MongoClient

from local_settings_hw_43 import MONGODB_URL_WRITE
from homework_43_01 import ProductRepository


def print_products(products: list[dict]) -> None:
    print("Updated products:")
    for product in products:
        print(f"- {product['name']} — ${product['price']:.2f}")


def main() -> None:
    with MongoClient(MONGODB_URL_WRITE) as client:
        repo = ProductRepository(client)

        updated_count = repo.increase_prices(percent=20)
        print(f"Prices updated for {updated_count} products.")
        print()

        print_products(repo.find_all())


if __name__ == "__main__":
    main()

# Prices updated for 3 products.
#
# Updated products:
# - Laptop — $1440.00
# - Mouse — $30.00
# - Keyboard — $84.00
