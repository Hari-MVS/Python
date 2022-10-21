nums_list = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 150, 100, 100, 20, 20]
n=int(input())
count=0
for i in nums_list:
    if n==i:
        count+=1
print(count)
