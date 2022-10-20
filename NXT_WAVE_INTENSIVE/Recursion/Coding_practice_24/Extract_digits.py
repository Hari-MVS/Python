n= input()
dig=[]
for i in n:
    if i.isdigit():
        dig+=[int(i)]
print(sum(dig))
print(min(dig))
print(max(dig))
