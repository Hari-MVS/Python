m = int(input())
        
for i in range(1,m+1):
    for j in range(1,i+1):
        print("* ",end='')
            
    print()
        
for i in range(1,m):
        print("* "*(m-i),end='')
        print()
