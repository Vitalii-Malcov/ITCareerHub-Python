import models

result = (
    models.session.query(models.Category.name, models.func.count(models.Product.id).label("product_count"))
    .join(models.Product)
    .group_by(models.Category.name)
    .having(models.func.count(models.Product.id) > 1)  # HAVING фильтрует уже сгруппированные данные
    .all()
)

for name, count in result:
    print(name, count)
