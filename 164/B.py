A,B,C,D = (int(x) for x in input().split())

for i in range(100):
    C =  C - B 
    if C <= 0:
        print("Yes")
        break
    else:
        A  = A - D
        if A <= 0:
            print("No")
            break


