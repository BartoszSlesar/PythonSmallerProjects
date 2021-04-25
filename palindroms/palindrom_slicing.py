def is_palindrom(arg):
    """ function check if provided string or integer is a palindrom using slicing"""
    if isinstance(arg, str) or isinstance(arg, int):
        arg = str(arg)
        if arg == arg[len(arg)::-1]:
            print(f"{arg} is a palindrom")
        else:
            print(f"{arg} is not a palindrom")
    else:
        raise ValueError("Provided argument is not int or string")



