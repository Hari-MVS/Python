a =[int(i) for i in (input().split(","))]
b= int(input())
print(*a[b:])
print(*a[:len(a)-b])
