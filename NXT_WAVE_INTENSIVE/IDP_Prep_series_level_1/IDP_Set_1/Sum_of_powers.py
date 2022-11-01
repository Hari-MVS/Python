n=input().split()

sum=0
for i in n:
    if len(i)<=1:
        sum+=0
    else:
        sum+=(int(i[:-1])**int(i[-1]))
print(sum)
            
