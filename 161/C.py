N,K = (int(x) for x in input().split())

a = N%K

if abs(K-a) > a:
    print(a)
else:
    print(abs(K-a) )




