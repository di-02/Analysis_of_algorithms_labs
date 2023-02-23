def Heap(array,n,i):
    biggest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and array[i] < array[l]:
        biggest = l
    if r < n and array[biggest] < array[r]:
        biggest = r
    if biggest != i:
        (array[i], array[biggest]) = (array[biggest], array[i])
        Heap(array, n, biggest)

def HeapSort(array,n):
    for i in range(n // 2 -1, -1, -1):
        Heap(array,n,i)

    for i in range(n -1 , 0, -1):
        (array[i], array[0]) = (array[0], array[i])
        Heap(array,i,0)

