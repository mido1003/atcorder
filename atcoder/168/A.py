s = input()

if s[-1] == "3":
    print("bon")
elif s[-1] == "0" or s[-1] == "1" or s[-1] == "6" or s[-1] == "8":
    print("pon")
elif s[-1] == "2" or s[-1] == "4" or s[-1] == "5" or s[-1] == "7" or s[-1] == "9":
    print("hon")