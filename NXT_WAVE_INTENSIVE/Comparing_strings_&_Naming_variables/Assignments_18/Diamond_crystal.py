m = int(input())
for i in range(0,m):
    print(" "*(m-i-1)+"/"+" "*(2*i)+"\\")
        
for i in range(0,m):
    print(" "*(i)+"\\"+" "*(2*(m-i-1))+"/")
