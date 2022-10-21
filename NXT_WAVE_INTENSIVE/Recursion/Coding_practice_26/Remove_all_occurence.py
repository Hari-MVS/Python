nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100]
new_list=[]
n = int(input())
for i in nums_list:
    if i ==n:
        continue
    else:
        new_list.append(i)
print(new_list)
