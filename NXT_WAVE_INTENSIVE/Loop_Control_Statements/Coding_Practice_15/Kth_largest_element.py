m = int(input())
n = int(input())
count= 0
largest= m
for i in range(1,m+1):
    if (m%largest==0):
        count+=1
            
    if (count==n):
        print(largest)
        break
            
    largest-=1
