def calculate_power(x, y):
    if y==1:
        return x
    else:
        return x*calculate_power(x,y-1)

a = int(input())
b = int(input())
print(calculate_power(a,b))
