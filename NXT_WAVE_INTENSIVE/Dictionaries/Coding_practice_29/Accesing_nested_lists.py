list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here
n=int(input())
new=[]
for i in range(n):
    m= [int(i) for i in input().split()]
    new.append(list_a[m[0]][m[1]])
print(new)
