def get_transpose_of_matrix(matrix, m, n):
    new=[]
    for i in range(n):
        tem=[]
        for j in range(m):
            tem.append(matrix[j][i])
        new.append(tem)
    return new


def print_max_min_sum_for_row_wise(num_list):
    max_val=[]
    min_val=[]
    sum_val=[]
    for i in num_list:
        max_val.append(max(i))
        min_val.append(min(i))
        sum_val.append(sum(i))
    print(max_val)
    print(min_val)
    print(sum_val)

        
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


# Write your code here
# get_transpose_of_matrix function()
print_max_min_sum_for_row_wise(get_transpose_of_matrix(num_list,m,n))
