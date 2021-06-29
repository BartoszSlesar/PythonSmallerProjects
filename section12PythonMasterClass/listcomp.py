print(__file__)

# comprehension can also be applied to sets use {} instead of []
squares = {num ** 2 for num in range(1, 7)}
print(type(squares), squares, sep=" : ")


def centre_text(*args):
    # bellow is generator expression
    text = "-".join(str(arg) for arg in args)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")

