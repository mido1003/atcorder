K = int(input())
A , B = (int(x) for x in input().split())


for i in range(1000):
    if B >= i * K >= A:
        print("OK")
        break
    elif i*K > B:
        print("NG")
        break

