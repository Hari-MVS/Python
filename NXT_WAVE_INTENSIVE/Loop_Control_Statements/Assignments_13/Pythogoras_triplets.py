a=int(input())
count=0
for i in range(1,a+1):
    for j in range(1,a+1):
        for k in range(1,a+1):
            if i<j<k:
                if k**2 ==(i**2+j**2):
                    count+=1
print(count)
