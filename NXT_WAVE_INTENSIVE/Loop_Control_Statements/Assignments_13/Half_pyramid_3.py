a = int(input())
b = int(input())
for i in range(1,b+1):
    for j in range(i):
        print(a,end=' ')
        a+=1
    print("")
