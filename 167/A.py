import re

s = input()
t = input()

match_result = re.match(s+".",t)

if match_result:
    print("Yes")
else:
    print("No")