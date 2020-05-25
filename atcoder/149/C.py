import math

x = int(input())
result = True
sum = 0

m = math.floor(math.sqrt(x)) + 1
for p in range(3, m, 2):
    if n % p == 0:
        result = False
        sum = p
        break

print(sum)