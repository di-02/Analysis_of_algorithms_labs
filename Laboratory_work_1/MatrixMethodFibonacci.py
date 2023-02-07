import time
import matplotlib.pyplot as plt


def Fibonacci(n):
    F = [[1,1],[1,0]]

    power(F,n-1)

    return F[0][0]

def multiply(F,M):

    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

def power(F,n):

    M = [[1,1],[1,0]]

    for i in range(2,n+1):
        multiply(F,M)

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

plt.plot(terms,exec,color = 'c', marker = 'o')
plt.xlabel('Number of terms')
plt.ylabel('Time in seconds')
plt.grid(True)
plt.title('Matrix method for Fibonacci numbers')
plt.show()
    
