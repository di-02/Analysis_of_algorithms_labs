def Eratosthenes_3(n):
    prime = []
    for i in range(n + 1):
        prime.append(True)

    prime[1] = False
    i = 2
    while i <= n:
        if prime[i]:
            j = i+1
            while j <= n:
                if j % i == 0:
                    prime[j] = False
                j = j + 1
        i = i + 1

