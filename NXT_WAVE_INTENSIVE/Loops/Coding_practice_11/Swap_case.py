a = input()
new=''
for i in a:
    if i.isupper():
        new+=i.lower()
    else:
        new+=i.upper()
print(new)
