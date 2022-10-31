n=input().split()
count=0
temp=[]
for i in n:
    od=''
    for j in i:
        if j.isdigit():
            od+=j
        else:
            if od:
                temp.append(int(od))
                od=''
                count+=1
    if od:
        temp.append(int(od))
        count+=1
            
print(sum(temp))
print(round((sum(temp)/count),2))
