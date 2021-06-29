import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print(f"my_range is returning {start}")
        yield start
        start += 1


# big_range = range(10000)
big_range = my_range(5)
print(next(big_range))
print(f"big_range is {sys.getsizeof(big_range)} bytes")

# create list containing all the values
big_list = [num for num in big_range]

print(f"big_list is {sys.getsizeof(big_list)} bytes")

print(big_range)
print(big_list)
