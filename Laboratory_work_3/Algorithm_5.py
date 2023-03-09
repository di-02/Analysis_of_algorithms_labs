import math
def Eratosthenes_5(n):
    prime = []
    for i in range (n + 1):
        prime.append(True)

    prime[1] = False
    i = 2
    while i <= n:
        j = 2
        while j <= math.pow(i,0.5):
            if i % j == 0:
                prime[i] = False
            j = j + 1
        i = i + 1




