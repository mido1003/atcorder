import math

A,B = (int(x) for x in input().split())
result = False
y = math.ceil(A * 12.5)
z = math.floor((A+1)*12.5)
#if B >= A:

for h in range(y,z):
    #print(h)
    if result == True:
        break

    for i in range(B*10 ,(B+1)*10):
       
        if i == h:
            result = True
            break
       
if result == True:
    print(i)
else:
    print(-1)

#else:
#    price1 = int(B / 10)

#    for i in range(math.ceil(A*12.5) ,math.floor((A+1)*12.5)):
#        print(i)
#        if price1 == i:
#            result = True
            #break
#    if result == True:
#        print(price1)
#    else:
#        print(-1)