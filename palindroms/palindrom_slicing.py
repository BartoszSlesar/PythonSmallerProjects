import re
from typing import Union


def is_palindrome(__arg: Union[int, str]) -> bool:
    """check if provided `arg` is palindrome.


    palindrome is word, phrase, or sequence that reads the same backwards as forwards.


    :param __arg: is a positional only argument of Type`string` or `int` that will be checked if it's a palindrome
        Sentences also ca be passed.
    :raises ValueError: when `arg` argument is not a `string` or `int` exception is raised.
    :return bool: function returns `True` if `arg` is palindrome `False` otherwise.
    """
    # regex to filter separators when multi text is passed
    separator = re.compile(r"[,'\s.\"?!]+")
    if isinstance(__arg, str) or isinstance(__arg, int):
        pal = str(__arg).lower()
        # filtering all text separators
        pal = separator.sub("", pal)
        result = False
        if pal == pal[len(pal)::-1]:
            print(f"{__arg} is a palindrom")
            result = True
        else:
            print(f"{__arg} is not a palindrom")
        return result
    else:
        raise ValueError("Provided argument is not int or string")
