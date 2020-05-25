n,k = (int(x) for x in input().split())
h = [int(x) for x in input().split()]
sum = 0
result = True
h.sort(reverse=True)

if k < n:
    for i in range(k,len(h)):
        sum += h[i]
else:
    result = False

if result:
    print(sum)
else:
    print(0)