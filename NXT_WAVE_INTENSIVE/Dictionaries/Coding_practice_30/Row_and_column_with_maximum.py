def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

new =[j for i in num_list for j in i]
great=max(new)
col=[]
for i in num_list:
    if great in i:
        print(i)
        temp=i.index(great)
        for i in range(m):
            col.append(num_list[i][temp])
        break
print(col)
