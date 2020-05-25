n = int(input())
h = [input() for i in range(n)]

kensaku = list(set(h))
result = 0
list = []
#print(kensaku)
for i in range(len(kensaku)):
    

    if h.count(kensaku[i]) > result:
        result = h.count(kensaku[i])
        list = []
        list.append(kensaku[i])
    elif h.count(kensaku[i]) == result:
        
        list.append(kensaku[i])
        

#print(list)
sorted(list)
for h in range(len(list)):
    print(list[h])