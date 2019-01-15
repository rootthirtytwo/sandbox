def linear_search(array, item):
    '''

    :param array: the list of items
    :param item: the value that need to be search
    :return: position of the of the of this item, if not found -1
    '''
    for i,v in enumerate(array):
        if item == v:
            return i
    return -1


if __name__=="__main__":
    my_list = [2,1,5,4,6,3,7]
    search_item = 9
    result = linear_search(my_list,search_item)
    print("Given list ", my_list)

    if result == -1:
        print("item {0} not found.".format(search_item))
    else:
        print("item {0} found at position {1}.".format(search_item, result))

