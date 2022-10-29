word=[i for i in input().split()]
k=int(input())
for i in word:
    if len(i)==k:
        continue
    else:
        print(i,end=' ')
