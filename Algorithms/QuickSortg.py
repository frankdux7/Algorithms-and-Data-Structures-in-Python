def partition(L, first, last):
    pivot = L[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and L[leftmark] <= pivot:
            leftmark += 1

        while rightmark >= leftmark and L[rightmark] >= pivot:
            rightmark -= 1

        if rightmark < leftmark:
           done = True
        else:
           temp = L[leftmark]
           L[leftmark] = L[rightmark]
           L[rightmark] = temp

    temp = L[first]
    L[first] = L[rightmark]
    L[rightmark] = temp

    return rightmark

def quickSortHelp(L, first, last):
    if first<last:
        split = partition(L, first, last)

        quickSortHelp(L, first, split - 1)
        quickSortHelp(L, split + 1 , last)

    return L

def quickSort(L):
    quickSortHelp(L, 0, len(L)-1)
    return L




my_list = [54,26,93,17,77,31,44,55,20]

print(quickSort(my_list))
