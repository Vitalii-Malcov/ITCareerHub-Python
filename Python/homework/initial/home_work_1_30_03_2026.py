
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a <= b and b <= c:
    print(a, b, c, sep=", ")
elif a <= c and c <= b:
    print(a, c, b, sep=", ")
elif b <= a and a <= c:
    print(b, a, c, sep=", ")
elif b <= c and c <= a:
    print(b, c, a, sep=", ")
elif c <= a and a <= b:
    print(c, a, b, sep=", ")
else:
    print(c, b, a, sep=", ")

#
# if (a <= b <= c):
#     print(a, b, c)
# elif (a <= c <= b):
#     print(a, c, b)
# elif (b <= a <= c):
#     print(b, a, c)
# elif (b <= c <= a):
#     print(b, c, a)
# elif (c <= a <= b):
#     print(c, a, b)
# elif (c <= b <= a):
#     print(c, b, a)
