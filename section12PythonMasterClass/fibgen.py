def fibonacci(n: int):
    current, previous = 0, 1
    for nth in range(n):
        yield current
        current, previous = current + previous, current


def infinite_odd_gen():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = infinite_odd_gen()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


approx_pi = pi_series()
for x in range(1000000):
    print(next(approx_pi))
