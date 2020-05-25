
A = [input().split() for i in range(3)]
N = int(input())

B = [input() for _ in range(N)]

result = False

for x in range(len(B)):
    for y in range(3):
        for z in range(3):
            #print(A)
            #print(B[x])
            if A[y][z] == B[x]:
                A[y][z] = 0

for i in range(3):
        if A[i][0] == A[i][1] == A[i][2]:
            result = True
            break

for i in range(3):
        if A[0][i] == A[1][i] == A[2][i]:
            result = True
            break

if A[0][0] == A[1][1] == A[2][2] or A[0][2] == A[1][1] == A[2][0]:
    result = True
    
#print(A)

if result == False:
    print("No")
else:
    print("Yes")


    