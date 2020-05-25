N,M = (int(x) for x in input().split())
list = [int(x) for x in input().split()]


sum = 0

for i in range(len(list)):
    sum = sum + list[i]

if N - sum < 0:
    print(-1)
else:
    print(N-sum)

