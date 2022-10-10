a= int(input())
b= int(input())
even =0
odd =0
for i in range(a,b+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(odd)
print(even)
