def join_handler(iterable, seperator):
    if iterable == []:
        return "<Nothing>"
    else:
        return seperator.join(iterable)
