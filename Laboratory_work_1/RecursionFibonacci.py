import time
import matplotlib.pyplot as plt


def Fibonacci(n):

   if n <= 1:
    return n
   else:
    return(Fibonacci(n-1) + Fibonacci(n-2))

exec = []
terms =[5,7,10,12,15,17,20,22,25,30,32,35,40]
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

plt.plot(terms,exec,color = 'g', marker = 'o')
plt.xlabel('Number of terms')
plt.ylabel('Time in seconds')
plt.grid(True)
plt.title('Recursion method for Fibonacci numbers')
plt.show()
    