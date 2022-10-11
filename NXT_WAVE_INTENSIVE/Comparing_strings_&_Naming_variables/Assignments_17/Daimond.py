m =int(input())
for i in range(1,m+1):
    print(". "*(m-i)+"0 "*(2*i-1)+". "*(m-i),end='')
    print()
        
for i in range(1,m):
    print(". "*(i)+"0 "*((2*m)-(2*i)-1)+". "*(i),end='')
    print()
