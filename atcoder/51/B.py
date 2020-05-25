K,S = (int(x) for x in input().split())
count = 0

for x in range(K+1):
    if x > S:
        break
    for y in range(K+1):
        z = S - x - y
        if 0 <= z <= K:
            count += 1
        elif x + y > S:
            break


print(count)