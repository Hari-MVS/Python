n= int(input())
l=[]
for i in range(n):
    m=input().split()
    if m[0] == 'insert':
        l.insert(int(m[1]),int(m[2]))
    elif m[0] == 'append':
        l.append(int(m[1]))
    elif m[0] == 'pop':
        l.pop()
    elif m[0] == "remove":
        l.remove(int(m[1]))
    elif m[0] == "sort":
        l.sort()
    elif m[0] == "print":
        print(l)
