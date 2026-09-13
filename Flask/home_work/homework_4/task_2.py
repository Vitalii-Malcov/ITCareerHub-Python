import models


categories = models.session.query(models.Category).all()

for category in categories:
    print(category.name)
    for product in category.products:  # ORM подгружает продукты через relationship
        print(f"  {product.name} - {product.price}")
