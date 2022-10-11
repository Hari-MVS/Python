m = int(input())
d=65
for i in range(1,m+1):
    
    print(" "*(m-i),end='')
    for j in range(1,i+1):
        if ( j==1 ):
            print(chr(d)+" ",end='')
        elif(j==i ):
            print(chr(d)+" ",end='')
        else:
            print("  ",end='')
    d+=1
                    
    print()
        
for i in range(2,m+1):
    d=65
    d=(d+m)-i
    print(" "*(i-1),end='')
    for j in range(1,m+1):
        if (j==1):
            print(chr(d)+" ",end='')
        elif (j==m-i+1):
            print(chr(d)+" ",end='')
                    
        else:
            print("  ",end='')
                
    d+=1           
            
    print()
