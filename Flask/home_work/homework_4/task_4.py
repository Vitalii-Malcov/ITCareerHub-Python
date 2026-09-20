import models

result = (
    models.session.query(models.Category.name, models.func.count(models.Product.id))
    .outerjoin(models.Product)
    .group_by(models.Category.name)
    .all()
)

for name, count in result:
    print(name, count)
