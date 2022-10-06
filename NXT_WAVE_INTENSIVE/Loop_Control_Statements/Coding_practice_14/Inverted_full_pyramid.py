m = int(input())
for i in range(0,m):
    print(" "*(i),end='')
    for j in range(1,m-i+1):
        print("* ",end='')
    print()
