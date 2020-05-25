A,B,C = (int(x) for x in input().split())

if A == B == C:
    print("No")
elif A == B and A != C:
    print("Yes")
elif A == C and A != B:
    print("Yes")
elif B == C and A != C:
    print("Yes")
elif B == C and A != B:
    print("Yes")
elif A != B != C:
    print("No")