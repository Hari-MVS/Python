a = int(input())
count=0
for i in range(2,a+1):
    if a%i==0:
        count+=1
print("True" if count>1 else "False")
