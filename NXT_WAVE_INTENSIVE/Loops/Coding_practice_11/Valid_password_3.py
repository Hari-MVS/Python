a = input()
lower=0
upper=0
digit=0
for i in a:
    if i.isdigit():
        digit+=1
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
if digit>=1 and lower >=1 and upper >=1:
    print("Valid Password")
else:
    print("Invalid Password")
