m = int(input())
for i in range(1,m+1):
    print(" "*(m-i),end='')
    for j in range(1,i+1):
        if ( j==1 ):
            print("* ",end='')
        elif(j==i or i==m ):
            print("* ",end='')
        else:
            print("  ",end='')
                    
                
                
            
    print()
