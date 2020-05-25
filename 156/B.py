n,k = (int(x) for x in input().split())

amari = []

while n != 0:
    amari.append(n%k)
    n = n // k

print(len(amari))
