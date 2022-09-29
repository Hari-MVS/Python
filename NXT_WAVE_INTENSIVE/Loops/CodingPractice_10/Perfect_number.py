a= int(input())
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
print("Perfect Number" if sum==a else "Not a Perfect Number")
    
