N,M = (int(x) for x in input().split())
hight = [int(x) for x in input().split()]
tenbou = [input().split() for l in range(M)]
result = [1] * N


for i in range(M):
    x = int(tenbou[i][0]) - 1
    y = int(tenbou[i][1]) - 1
    if hight[x] > hight[y]:
        result[y] = 0
    elif hight[y] == hight[x]:
        result[x] = 0
        result[y] = 0
    elif hight[y] > hight[x]:
        result[x] = 0
#print(result)
print(result.count(1))