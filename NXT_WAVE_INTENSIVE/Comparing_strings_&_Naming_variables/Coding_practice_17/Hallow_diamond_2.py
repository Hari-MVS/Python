m = int(input())
med =2*m;
for i in range(0,m):
    print("* "*(m-i)+"  "*(2*i)+"* "*(m-i),end='')
    print()
        
for j in range(1,m+1):
    print("* "*(j)+"  "*(med-(2*j))+"* "*(j),end='')
    print()
