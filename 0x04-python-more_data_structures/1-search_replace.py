def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, n in enumerate(my_list):
        if n == search:
            new_list[i] = replace
    return new_list
