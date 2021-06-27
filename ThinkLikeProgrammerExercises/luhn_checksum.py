def get_int():
    while True:
        value = 0
        try:
            value = input("Enter number: ")
            if not value.isdigit():
                raise ValueError
        except ValueError:
            print(value, " is not digit")
        else:
            return value


def luhn_checksum(number: str) -> bool:
    """check if number is valid according to luhn checksum formula

        :param number: number in str' format that will be checked
        :return: return True` if valid otherwise False`
    """

    def double_digit(digit):
        x = digit * 2
        return (x % 10) + 1 if x > 10 else x

    # another solution, when length is not known, simultaneously count double of odd and even numbers
    odd = 0
    even = 0
    for i, num in enumerate(number, 1):
        n = int(num)
        if i % 2 != 0:
            even += double_digit(n)
        else:
            even += n
        if i % 2 == 0:
            odd += double_digit(n)
        else:
            odd += n
    check_value = even if (len(number) % 2 == 0) else odd
    return check_value % 10 == 0


if __name__ == '__main__':
    # num = get_int()
    check = [1, 7, 6, 2, 4, 8, 3]
    print(luhn_checksum(check))
