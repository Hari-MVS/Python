m = int(input())
print(". "*(m-1)+"0 "+". "*(m-1))
for i in range(1,m):
    print(". "*(m-i-1)+"0 "*(i*2+1)+". "*(m-i-1))
        
