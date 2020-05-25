n,k,m = (int(x) for x in input().split())
a = [int(x) for x in input().split()]



sum = sum(a)
result = True



for i in range(k+1):
    if i >= n*m-sum:
        print(i)
        result = False
        break

if result:
    print(-1)
