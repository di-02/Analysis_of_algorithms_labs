import time
import matplotlib.pyplot as plt

def Fibonacci(n):
    first = 0
    second = 1
    if n > 1:
        for i in range(2,n+1):
            mid = first + second
            first = second
            second = mid
        return second

exec = []
terms =[5,7,10,12,15,17,20,22,25,30,32,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
print('Number of terms: ',terms)
for j in range(len(terms)):
    #set current time
    currTime = time.time()
    Fibonacci(terms[j])
    #end time
    end = time.time()
    #execition time
    exec.append(end - currTime)

print('Time of execution: ',exec)

plt.plot(terms,exec,color = 'm', marker = 'o')
plt.xlabel('Number of terms')
plt.ylabel('Time in seconds')
plt.grid(True)
plt.title('Spaced Optimized method for Fibonacci numbers')
plt.show()
    
