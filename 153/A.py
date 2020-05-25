H , A = (int(x) for x in input().split())
count = 0

while H > 0:
    H = H - A
    count += 1


print(count)