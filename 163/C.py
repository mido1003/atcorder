N = int(input())
list = [int(x) for x in input().split()]

result = [0] * N

#print(list)

for i in range(N-1):
    #print(list[i])
    result[list[i]-1] = result[list[i]-1] + 1 

#print(result)

for i in range(N):
    print(result[i])

#print(list)
