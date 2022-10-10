a = input()
gren=0
re=0
for i in a:
    if i=="G":
        gren+=1
    else:
        re+=1
print(re if re<gren else gren)
