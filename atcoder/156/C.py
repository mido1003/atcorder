import statistics
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

n = int(input())

x = [int(x) for x in input().split()]

mean = statistics.mean(x)

syukai = Decimal(str(mean)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

#print(syukai)

sum = 0

for i in range(len(x)):
    sum += (x[i] - syukai)**2

print(sum)