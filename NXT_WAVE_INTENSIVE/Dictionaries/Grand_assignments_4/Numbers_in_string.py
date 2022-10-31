n=input()
summ=0
count=0
for i in n:
    if i.isdigit():
        count+=1
        summ+=int(i)
print(summ)
print(round((summ/count),2))
