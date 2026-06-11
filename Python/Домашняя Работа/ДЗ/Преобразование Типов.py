

print("\n / int → float / str / bool /")
x = 10
print(float(x))   # 10.0
print(str(x))     # "10"
print(bool(x))    # True


print("\n / float → int / str / bool /")
x = 9.7
print(int(x))     # 9 (обрезает)
print(str(x))     # "9.7"
print(bool(x))    # True


print("\n / str → int / float /")
x = "10"
print(int(x))     # 10
print(float(x))   # 10.0


print("\n / str → bool /")
print(bool(""))      # False
print(bool("Hi"))    # True


print("\n / bool → int / float / str /")
print(int(True))     # 1
print(int(False))    # 0
print(float(True))   # 1.0
print(float(False))  # 0.0
print(str(True))     # "True"


print("\n / input всегда строка /")
x = input("Введите число: ")
print("Тип:", type(x))


print("\n / интересные случаи /")
print(bool(0))      # False
print(bool(-1))     # True
print(bool(0.0))    # False
print(int(True))    # 1
print(int(False))   # 0

