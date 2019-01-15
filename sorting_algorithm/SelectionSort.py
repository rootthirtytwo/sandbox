def selection_sort(mylist):
    '''

    :param mylist: unsorted list
    :return: sorted list
    '''

    for i in range(len(mylist)):

        first_item = i

        for j in range(i, len(mylist)):
            if mylist[j] < mylist[first_item]:
                first_item = j
        mylist[i],mylist[first_item] = mylist[first_item], mylist[i]

    return mylist

if __name__ == "__main__":

    lst = [2,5,1,3,4]

    print("Umsorted list : ", lst)
    print("Sorted list :", selection_sort(lst))

    # time complexity O(n^2)

