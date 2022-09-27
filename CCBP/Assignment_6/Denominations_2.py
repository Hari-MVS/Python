num= int(input())
a= num//100
num %=100
b=num//50
num %=50
c=num//20
num %=20
d=num//10

print("100 Notes:",a)
print("50 Notes:",b)
print("20 Notes:",c)
print("10 Notes:",d)
