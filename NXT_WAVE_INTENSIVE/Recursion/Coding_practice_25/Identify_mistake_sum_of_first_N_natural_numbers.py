def sum_of_numbers(n):
    if n == 0:  # Base case
        return n
    else:
        return n + sum_of_numbers(n-1)  # Recursion


num = int(input())
result = sum_of_numbers(num)
print(result)
