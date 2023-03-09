def Eratosthenes_2(n):
    prime = []
    for i in range(n + 1):
        prime.append(True)

    prime[1] = False
    i = 2
    while i <= n:
        j = 2*i
        while j <= n:
            prime[j] = False
            j = j + i
        i = i + 1


