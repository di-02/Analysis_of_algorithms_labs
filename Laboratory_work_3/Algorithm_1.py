def Eratosthenes_1(n):
    prime = []
    for i in range(n+1):
        prime.append(True)
    i = 2
    prime[1] = False
    while i <= n:
        if prime[i]:
            j = 2*i
            while j <= n:
                prime[j] = False
                j = j + i
        i = i + 1







