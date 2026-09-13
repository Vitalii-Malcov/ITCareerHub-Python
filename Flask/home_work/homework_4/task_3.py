import models

smartphone = models.session.query(models.Product).filter_by(name="Смартфон").first()
smartphone.price = 349.99
models.session.commit()
