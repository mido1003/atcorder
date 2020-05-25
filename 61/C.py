s = input()

sum = 0

if len(s) > 1:

    l = ["+"] * (len(s) - 1)

    n = 2 ** (len(s) - 1)

    for i in range(n):
        l = ["+"] * (len(s) - 1)
        for j in range(len(l)):
            ls = list(s)
            if (i >> j) & 1:
                l[j] = ""
            for x in range(len(l)):
                
                ls.insert(2*x+1,l[x])
    
        

        maped_list = map(str, ls) 
        mojiretu = ''.join(maped_list)

        sum = sum + eval(mojiretu)

    print(sum)
else:
    print(s)    



    
    
   



