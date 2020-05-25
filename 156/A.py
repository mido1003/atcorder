N,R = (int(x) for x in input().split())
 
if N >= 10:
    print(R)
else:
    print(R+(10- N)*100) 