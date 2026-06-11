import dis
import time
from timeit import timeit

x = timeit('dict()')
y = timeit('{}')

print(x)
print(y)

print(dis.dis('dict()'))
print(dis.dis('{}'))


