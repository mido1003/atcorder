N,K = (int(x) for x in input().split())
a = [input().split() for l in range(K * 2)]

list = [0] * N

for i in range(1,len(a),2):
    for n in range(len(a[i])):
        x = int(a[i][n])
        list[(x-1)] = 1
        


print(list.count(0))