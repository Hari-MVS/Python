def sum_of_squares_m_to_n(m, n):
    sum=0
    for i in range(m,n+1):
        sum+=i**2
    return sum

m = int(input())
n = int(input())
print(sum_of_squares_m_to_n(m,n))
