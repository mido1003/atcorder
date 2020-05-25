h,n = (int(x) for x in input().split())

a = [int(x) for x in input().split()]

if h > sum(a):
    print("No")
else:
    print("Yes")


#print(sum(a))