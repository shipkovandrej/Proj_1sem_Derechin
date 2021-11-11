def Kcheck(K):
    res = 0
    while K > 0:
        res += K
        K -= 1
    return res
N = int(input("chislo N: "))
K = N
while K > 0:
    print("novaya iteratsia")
    print("K ravno= ", K)

    if Kcheck(K) <= N:
        num = K
        break
    K -= 1
print(num)