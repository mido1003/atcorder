n = int(input())
a = [int(x) for x in input().split()]

result = True

a.sort()

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        result = False
        break

if result:
    print("YES")
else:
    print("NO")