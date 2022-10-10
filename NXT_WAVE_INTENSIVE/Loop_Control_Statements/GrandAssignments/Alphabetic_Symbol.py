a = int(input())

for i in range(a):
    b=65
    for j in range(i+1):
        print(chr(b),end=' ')
        b+=1
    print()
