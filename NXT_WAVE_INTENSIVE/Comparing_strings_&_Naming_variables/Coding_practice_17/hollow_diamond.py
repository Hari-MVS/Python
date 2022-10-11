m = int(input())
for i in range(1,m+1):
    print(" "*(m-i),end='')
    for j in range(1,i+1):
        if ( j==1 ):
            print("* ",end='')
        elif(j==i ):
            print("* ",end='')
        else:
            print("  ",end='')
                    
    print()
        
for i in range(2,m+1):
    print(" "*(i-1),end='')
    for j in range(1,m+1):
        if (j==1):
            print("* ",end='')
        elif (j==m-i+1):
            print("* ",end='')
                    
        else:
            print("  ",end='')
                
                
            
    print()
