import sys
import math

a,b,h,m = (float(x) for x in input().split())

zi = 0.5 * 60 * h + 0.5 * m
hun = 6 * m

if hun - zi > 180:
    degree = 360 - hun + zi
elif hun - zi < 180:
    degree = hun - zi
elif hun - zi == 180:
    print(a + b)
    sys.exit(0)

elif hun == zi:
    if b >= a:
        print(b - a)
        sys.exit(0)
    else:
        print(a-b)
        sys.exit(0)

cosain = math.cos(math.radians(degree))

print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * abs(cosain)))

