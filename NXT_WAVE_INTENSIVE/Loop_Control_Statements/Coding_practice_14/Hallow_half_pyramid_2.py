m = int(input())
for i in range(1,m+1):
    for j in range(1,m+1):
        if ( j==1 ):
            print(str(j)+" ",end='')
        elif(j==i or i==m ):
            print(str(j)+" ",end='')
        else:
            print("  ",end='')
                    
                
            
    print()
