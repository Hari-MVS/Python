a=input()
if a.isdigit():
    print("Digit")
elif a.isalpha():
    print("Uppercase Letter")
elif a.islower():
    print("Lowercase Letter")
else:
    print("Special Character")
