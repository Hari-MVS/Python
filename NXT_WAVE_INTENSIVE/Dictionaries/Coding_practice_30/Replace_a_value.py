def replace_old_value_with_new_value(matrix, old_value, new_value):
    for i in matrix:
        for j in i:
            if j==old_value:
                i[i.index(old_value)]=new_value
    [print(i) for i in matrix]


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

values = input().split()
old_value, new_value = convert_string_to_int(values)

replace_old_value_with_new_value(num_list,old_value,new_value)
# Write your code here
