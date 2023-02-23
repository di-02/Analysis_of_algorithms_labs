def Merge(array,l,m,r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = array[l + i]

    for j in range(0, n2):
        R[j] = array[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def MergeSort(array,l,r):
    if l < r:
        m = l + (r - l) // 2
        MergeSort(array, l, m)
        MergeSort(array, m + 1, r)
        Merge(array, l, m, r)