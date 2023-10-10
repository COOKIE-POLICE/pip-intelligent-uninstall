def join_handler(iterable, separator):
    if iterable == []:
        return "<Nothing>"
    else:
        return separator.join(iterable)
