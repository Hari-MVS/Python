n = int(input())
for  i in range(n+1):
    print("_",end="")
print()
for j in range(n):
    print("|",end="")   
    print(" "*(n-j-1),end="")   
    print("/")   
