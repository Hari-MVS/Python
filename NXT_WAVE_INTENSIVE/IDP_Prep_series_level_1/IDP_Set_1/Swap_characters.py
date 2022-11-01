a=list(input())
b=list(input())
if a==b:
    print('Yes')
if len(a)!=len(b):
    print('No')
else:
    for i in range(len(b)):
        if a[i]==b[i]:
            continue
        else:
            if i<len(b):
                temp=b[i]
                b[i]=b[i+1]
                b[i+1]=temp
            if a==b:
                print('Yes')
                break
            else:
                print('No')
                break
