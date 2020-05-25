ok = True

NM = [map(int, input().split())]
N, M = [list(i) for i in zip(*NM)]

l = [-1] * N[0]

if M[0] != 0:
    sc = [map(int, input().split()) for _ in range(M[0])]
    s, c = [list(i) for i in zip(*sc)]

    for i in range(M[0]):
        if l[s[i]-1] == -1:
            l[s[i]-1] = c[i]
        elif l[s[i]-1] != c[i]:
            ok = False
            break
        
if l[0] == 0 and N[0] >= 2:
    ok = False
elif l[0] == -1:
    if N[0] >= 2:
        l[0] = 1
    else:
        l[0] = 0
    
for i in range(1,N[0]):
    if l[i] == -1:
        l[i] = 0
    
ans = ""   
if ok:
    for i in range(len(l)):
        ans = ans + str(l[i])
    print(ans)
else:
    print("-1")

#print(M[0],N[0])
#print(s[0],c[0])