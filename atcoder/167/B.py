a,b,c,k = (int(x) for x in input().split())

ls = []

result = 0

for i in range(a):
    ls.append(1)

for i in range(b):
    ls.append(0)

for i in range(a):
    ls.append(-1)

sorted(ls, reverse=True)

for k in range(k):
    if ls[k] >
    result += ls[k]
    
ans = (k - a - b) * c

print(result)


if a >= k:
    print(k * 1)
