def InsertionSort(array,n):
    for i in range(0,n):
        a = array[i]
        j = i - 1
        while j >= 0 and a < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = a