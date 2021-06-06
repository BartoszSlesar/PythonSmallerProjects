def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a `string` centered between ** characters


    :param text: The text that will be centered.
        An asterisk (*) wil result in a row of asterisks
        width of `screen_width`. The default will print spaces
        width ** of ether sides.
    :param screen_width: This parameter will determine the max width of printed text
    :raises ValueError: when length of provided text is longer then `screen_width`-4
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)