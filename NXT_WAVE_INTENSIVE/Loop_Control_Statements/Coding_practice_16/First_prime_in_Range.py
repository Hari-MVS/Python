a=int(input())
b=int(input())
flag=False
for i in range(a,b+1):
    flag = False
    if abs(i)==1 :
        i+=1
    for j in range(2,b+1):
        if i==j:
            break
        elif i%j==0:
            flag=True
    if flag==False:
        print(i)
        break
    elif i==b and flag==True:
        print("No prime numbers in the given range")
