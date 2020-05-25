N = int(input())
A = [int(x) for x in input().split()]

result = True


for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 != 0 and A[i] % 5 != 0:
            result = False
            break
            

if result == True:
    print("APPROVED")
else:
    print("DENIED")
