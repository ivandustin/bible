def ord_keys(dictionary):
    return dict(zip(map(ord, dictionary.keys()), dictionary.values()))
