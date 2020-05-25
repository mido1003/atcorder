N,M = (int(x) for x in input().split())
list = [int(x) for x in input().split()]

sum = 0
result = 0

for i in range(N):
    sum = sum + list[i] 

for i in range(N):
    #print(list[i])
    if list[i] >= sum/4/M:
        result = result + 1
#print(result)
#print(sum/4)
if result >= M:
    print("Yes")
else:
    print("No")
