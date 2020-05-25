S = list(input())

zenhan = []
kouhan = []
result1 = True
result2 = True
result3 = True


for i in range(len(S)//2):
    zenhan.append(S[i])

for i in range(len(S)//2+1,len(S)):
    kouhan.append(S[i])

for i in range(len(S)//2):
    if S[i] != S[len(S)-i-1]:
        result1 = False
        break

for i in range(len(zenhan)//2):
    if zenhan[i] != zenhan[len(zenhan)-i-1]:
        result2 = False
        break

for i in range(len(kouhan)//2):
    if kouhan[i] != kouhan[len(kouhan)-i-1]:
        result3 = False
        break
#print(zenhan)
#print(kouhan)
#print(result1,result2,result3)

if result1 and result2 and result3:
    print("Yes")
else:
    print("No")