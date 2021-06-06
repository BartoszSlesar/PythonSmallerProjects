number = input("Please enter three numbers separated by comma: ")
data = number.split(",")
if len(data) == 3:
    # simple program to calculate a+b-c from user input using map
    numbers = map(int, data)
    a, b, c = numbers
    print(a + b - c)

    # simple program to calculate a+b-c from user using list comprehension
    numbers = [int(item) for item in data]
    a, b, c = numbers
    print(a + b - c)
else:
    print("You provided more than three numbers")
