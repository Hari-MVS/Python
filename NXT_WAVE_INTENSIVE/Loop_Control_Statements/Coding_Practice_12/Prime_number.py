a = int(input())
flag = False
for i in range(2,a+1):
    if i==a:
        break
    elif a%i==0:
        flag=True
            
if flag==False:
    print("Prime Number")
else:
    print("Not a Prime Number")
