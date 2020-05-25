import numpy as np

n,m,x = (int(x) for x in input().split())

goal = [ list(map(int,input().split(" "))) for i in range(n)]
okane = 10 ** 5 + 1
sum = []
#print(goal)

for j in range(2 ** n):
    ll = []
    ls = ["+"] * n
    result = []
    for k in range(len(ls)):
        if (j >> k) & 1:
            ls[k] = "-"

    #print(ls)    
    #print(ll)

    for h in range(n):
        
        #print(ls[h])
        if ls[h] == "+":
            ll.append(goal[h])
    #print(ll)


    result = np.sum(ll,axis=0,keepdims=True)
    #print(result)

    if len(ll) > 0:
        hantei = True
        for i in range(2):
            if result[0][i+1] < x :
                hantei = False

        if hantei == True and okane > result[0][0]:
            okane = result[0][0]     

if okane == 10 ** 5 + 1:
    print(-1)
else:
    print(okane)

 
    

    
      

