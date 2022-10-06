m = int(input())
for i in range(1,m+1):
    print(" "*(i-1),end='')
    for j in range(1,m+1):
        if ( i==1 or j==1):
            print(str(j)+" ",end='')
        elif(j==m-i+1):
            print(str(j)+" ",end='')
        else:
            print("  ",end='')
                    
                
                
            
    print()
