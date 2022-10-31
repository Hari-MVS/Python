n=input()
m=input()
flag=False
count=0
for i in range(len(m)):
    if m==n:
        flag=True
        break
    m=m[1:]+m[0]
    count+=1
print(count if flag==True else 'No Match')
