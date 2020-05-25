N,A,B = (int(x) for x in input().split())

Kurikaeshi = N // (A + B) 
Amari = N % (A + B)
Aoi = 0 

if Amari >= A:
    Aoi = A
else:
    Aoi = Amari

result = Aoi + Kurikaeshi * A


print(result)
