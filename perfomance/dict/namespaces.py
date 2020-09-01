# page 103
import time
import math
from math import sin

def test1(x):
    return math.sin(x)

def test2(x):
    return sin(x)

def test3(x, localsin=math.sin):
    return localsin(x)

start = time.time()
test = [test1(i) for i in range(10000000)]
end = time.time()
print(end-start)

start = time.time()
test2 = [test2(i) for i in range(10000000)]
end = time.time()
print(end-start)

start = time.time()
test3 = [test3(i) for i in range(10000000)]
end = time.time()
print(end-start)