
mb = int(input("Введите использованные мегабайты: "))


extra = (mb - 500) * (mb > 500)


#--total = 30 + extra * 0.2

total = (extra > 0 and (30 + extra * 0.2)) or 30


print("Общая стоимость:", total)
