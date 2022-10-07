m = int(input())
for i in range(1,m+1):
    for j in range(1,m+1):
        if (i==1 or j==1 or j==m ):
            print("* ",end='')
        else: 
            print("  ",end='')
            
            
    print()
        
for i in range(0,m+1):
    for j in range(1,m+1):
        if (i==0 or j==1 or j==m or i==m):
            print("* ",end='')
        else : 
            print("  ",end='')
                
            
    print()
