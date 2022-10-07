m = int(input())
print("0 "*(m-1)+"1 "+"0 "*(m-1))
for i in range(1,m):
    print("0 "*(m-i-1)+"1 "*(i*2+1)+"0 "*(m-i-1))
