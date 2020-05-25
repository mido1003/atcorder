K,N = (int(x) for x in input().split())
house = list(map(int,input().split()))

distance = []


for i in range(N-1):
    distance.append(house[i+1] - house[i])
    
distance.append(K - house[N-1] + house[0]) 



print(K-max(distance))