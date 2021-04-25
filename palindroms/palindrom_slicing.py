def is_palindrom(arg):
    """ function check if provided string or integer is a palindrom using slicing"""
    if isinstance(arg, str) or isinstance(arg, int):
        pal = str(arg).lower()
        result = False
        if pal == pal[len(pal)::-1]:
            print(f"{arg} is a palindrom")
            result = True
        else:
            print(f"{arg} is not a palindrom")
        return result
    else:
        raise ValueError("Provided argument is not int or string")
