a = int(input())

for i in range(a):
    print(" "*(a-1-i)+"* "*(i+1))
for j in range(2,a+1):
    print(" "*(j-1)+"* "*(a-j+1))
