import time
import matplotlib.pyplot as plt

memoiz = {0: 0, 1:1}

def Fibonacci(n):
    if n in memoiz:
        return memoiz[n]
    memoiz[n] = Fibonacci(n-1) + Fibonacci(n-2)

exec = []
terms =[5,7,10,12,15,17,20,22,25,30,32,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
print('Number of terms: ',terms)
for j in range(len(terms)):
    #set current time
    currTime = time.time()
    for i in range(terms[j]):
        Fibonacci(i)
    #end time
    end = time.time()
    #execition time
    exec.append(end - currTime)

print('Time of execution: ',exec)

plt.plot(terms,exec,color = 'k', marker = 'o')
plt.xlabel('Number of terms')
plt.ylabel('Time in seconds')
plt.grid(True)
plt.title('Memoizing method for Fibonacci numbers')
plt.show()
    
