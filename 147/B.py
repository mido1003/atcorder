s = str(input())

rslt = s[::-1]

count = 0

if len(s)%2==0:

    for i in range(len(s)//2):

        if s[i] != rslt[i]:
            count += 1
else:
     for i in range(len(s)//2):

        if s[i] != rslt[i]:
            count += 1

           



print(count)