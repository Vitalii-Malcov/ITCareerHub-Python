import models


electronics = models.get_or_create_category("Электроника", "Гаджеты и устройства.")
books = models.get_or_create_category("Книги", "Печатные книги и электронные книги.")
clothes = models.get_or_create_category("Одежда", "Одежда для мужчин и женщин.")

models.get_or_create_product("Смартфон", 299.99, True, electronics)
models.get_or_create_product("Ноутбук", 499.99, True, electronics)
models.get_or_create_product("Научно-фантастический роман", 15.99, True, books)
models.get_or_create_product("Джинсы", 40.50, True, clothes)
models.get_or_create_product("Футболка", 20.00, True, clothes)
