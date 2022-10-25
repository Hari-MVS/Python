num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
n=int(input())
new=[]
for i in num_list:
    new.append(i[:-1]+(n,))
print(new)
