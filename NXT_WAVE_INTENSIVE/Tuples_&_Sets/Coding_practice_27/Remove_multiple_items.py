num_set = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
# Write your code here
n=[int(i) for i in input().split(' ')]
new=[]
for i in list(num_set):
    if i not in n:
        new.append(i)
print(sorted(new))
