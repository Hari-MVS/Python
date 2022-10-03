
n = int(input())
for i in range(1,n+1):
    if (i==1 or i==n):
        print("* "*(n))
    else:
        print("* "*(1)+"  "*(n-2)+"* "*(1))
            
        
for i in range(1,n):
    if (i==n-1):
        print("* "*(n))
    else:
        print("  "*(n-1)+"* "*(1))
