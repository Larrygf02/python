from math import sin
import time

def tight_loop_slow(iterations):
    result = 0
    for i in range(iterations):
        # este llamado requiere una busqueda global
        result += sin(i)

def tight_loop_fast(iterations):
    result = 0
    local_sin = sin
    for i in range(iterations):
        result += local_sin(i)

start = time.time()
print(tight_loop_slow(10000000))
end = time.time()
print(end-start)

start = time.time()
print(tight_loop_fast(10000000))
end = time.time()
print(end-start)

