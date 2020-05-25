import math

N,M = (int(x) for x in input().split())

#result = math.factorial(N + M) - (N * M)

sum = math.factorial(N + M) // (math.factorial(N + M - 2) * math.factorial(2))


print(sum - N * M)