import matplotlib.pyplot as plt
import Algorithm_1 as a1
import Algorithm_2 as a2
import Algorithm_3 as a3
import Algorithm_5 as a5
import time
execTime = []
n = 700
current = time.time()
a1.Eratosthenes_1(n)
after = time.time()
execTime.append(after - current)
current = time.time()
a2.Eratosthenes_2(n)
after = time.time()
execTime.append(after - current)
current = time.time()
a3.Eratosthenes_3(n)
after = time.time()
execTime.append(after - current)
current = time.time()
a5.Eratosthenes_5(n)
after = time.time()
execTime.append(after - current)
print(execTime)
data = {'Algorithm 1':execTime[0],'Algorithm 2':execTime[1],'Algorithm 3':execTime[2],'Algorithm 5':execTime[3]}
algorithms = list(data.keys())
timeExecution = list(data.values())
plt.bar(algorithms,timeExecution, color = 'maroon', width = 0.4)
plt.xlabel('Algorithms')
plt.ylabel('Time of execution')
plt.title('4 algorithms for Eratosthenes sieve to get all primes less than 700')
plt.show()
