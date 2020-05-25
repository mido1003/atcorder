N , Y = (int(x) for x in input().split())
senen = Y//10000
result = False
gosenen = Y // 5000

for x in range(N, -1, -1):
    #Y = Y - 10000 * x
    #print("x:",x)
    for y in range(N,-1,-1):
        #Y = Y - y * 5000
        z = N - x - y
        if x * 10000 + y * 5000 + z * 1000 == Y and x + y + z <= N and z >= 0:
            result = True
            print(x,y,z)
            break
    else:
        continue
    break





if result == False:
    print(-1,-1,-1)