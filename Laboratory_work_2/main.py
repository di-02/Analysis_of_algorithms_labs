import QuickSort
import InsertionSort
import MergeSort
import HeapSort
import random
import matplotlib.pyplot as plt
import time
n = 1
QuickTime = []
InsertTime = []
MergeTime = []
HeapTime = []
terms = []
for i in range(12):
    n = n * 3
    terms.append(n)
n = 1
for x in range(12):
    data = []
    n = n * 3
    copy1 = []
    copy2 = []
    copy3 = []
    copy4 = []
    for i in range(n):
        data.append(random.randint(1,1000))
    copy1 = data
    copy2 = data
    copy3 = data
    copy4 = data
    currTime = time.time()
    QuickSort.QuickSort(copy1,0,n-1)
    endTime = time.time()
    QuickTime.append(endTime - currTime)
    currTime = time.time()
    InsertionSort.InsertionSort(copy2,n)
    endTime = time.time()
    InsertTime.append(endTime - currTime)
    currTime = time.time()
    HeapSort.HeapSort(copy3,n)
    endTime = time.time()
    HeapTime.append(endTime - currTime)
    currTime = time.time()
    MergeSort.MergeSort(copy4,0,n-1)
    endTime = time.time()
    MergeTime.append(endTime - currTime)
print(QuickTime)
print(InsertTime)
print(MergeTime)
print(HeapTime)
print(terms)
fig, ax = plt.subplots(2,2)
ax[0,0].plot(terms,QuickTime, color = "red", linewidth = 2)
ax[0,1].plot(terms,InsertTime,color = "pink", linewidth = 2)
ax[1,0].plot(terms,MergeTime, color = "green", linewidth = 2)
ax[1,1].plot(terms,HeapTime,color = "blue", linewidth = 2)
ax[0,0].set_xlabel("Number of elements", fontsize = 8)
ax[0,1].set_xlabel("Number of elements", fontsize = 8)
ax[1,0].set_xlabel("Number of elements", fontsize = 8)
ax[1,1].set_xlabel("Number of elements", fontsize = 8)
ax[0,0].set_ylabel("Time", fontsize = 8)
ax[0,1].set_ylabel("Time", fontsize = 8)
ax[1,0].set_ylabel("Time", fontsize = 8)
ax[1,1].set_ylabel("Time", fontsize = 8)
ax[0,0].set_title("QuickSort", fontsize = 8)
ax[0,1].set_title("InsertionSort", fontsize = 8)
ax[1,0].set_title("MergeSort", fontsize = 8)
ax[1,1].set_title("HeapSort", fontsize = 8)
ax[0,0].grid(True)
ax[0,1].grid(True)
ax[1,0].grid(True)
ax[1,1].grid(True)
plt.show()





