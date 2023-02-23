def SelectionSort(array,n):
    for x in range(n):
        mid = x
        for i in range(x + 1,n):
            if array[i] < array[mid]:
                mid = i
        (array[x],array[mid]) = (array[mid],array[x])