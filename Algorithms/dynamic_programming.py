import time
fibrun = 30

def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


calculations = 0
@timing
def runFib1(n):
    return fib(n)
@timing
def runFib2(n):
    return fib2(n)


def fib(n):
    global calculations
    calculations+=1
    if(n<2):
        return n
    else:
        return fib(n-1) + fib(n-2)


print(f"Result Slow                -> {runFib1(fibrun)}")
print(f"Calculations done          -> {calculations}")
calculations = 0
cache = {}

def fib2(n):
    global calculations
    global cache
    calculations+=1
    if(n in cache):
        return cache[n]
    else:
        if n<2:
            return n
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]



print(f"Result Dynamic Programmin  -> {runFib2(fibrun)}")
print(f"Calculations done          -> {calculations}")
