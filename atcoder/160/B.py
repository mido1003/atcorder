X = int(input())

sen = X//500
X = X - sen * 500
go = X//5

print(sen*1000+5*go)