def factorial(n: int) -> int:
    """
    return factorial of number `n`

    Function that will calculate factorial of number `n` passed as argument (`n`!)

    :param n: its an `int` passed as argument to factorial function

    :returns: return factorial of number `n`
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
