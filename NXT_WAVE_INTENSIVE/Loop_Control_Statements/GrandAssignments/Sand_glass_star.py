m = int(input())
for i in range(0,m):
    print(" "*(i),end='')
    for j in range(1,m-i+1):
        print("* ",end='')
    print()

for i in range(2,m+1):
    print(" "*(m-i),end='')
    for j in range(1,i+1):
        print("*"+" ",end='')
                
            
    print()
