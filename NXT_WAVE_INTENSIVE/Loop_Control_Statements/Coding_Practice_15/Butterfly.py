m = int(input())
for i in range(1,m+1):
    print("* "*(i)+"  "*(2*m-2*i)+"* "*(i))
        
for i in range(m,0,-1):
    print("* "*(i)+"  "*(2*m-2*i)+"* "*(i))
