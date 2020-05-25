n = int(input())
s,t = input().split()

list = []

for i in range(n):
    list.append(s[i])
    list.append(t[i])

mojiretu = ''.join(list)
print(mojiretu)