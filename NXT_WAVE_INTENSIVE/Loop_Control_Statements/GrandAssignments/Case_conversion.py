a = input()
up=0
b=''
for i in a:
    if i.isupper():
        up+=1
        if up>=2:
            b+='_'
        b+=i.lower()
    else:
        b+=i
print(b)
