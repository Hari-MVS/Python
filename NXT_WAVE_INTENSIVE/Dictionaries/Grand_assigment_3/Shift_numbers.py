string=input()
digits=''
characters=''
for i in string:
    if i.isdigit():
        digits+=i
    else:
        characters+=i
print(characters+digits)
