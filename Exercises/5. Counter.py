def counter(n):
    count = {}
    for i in n:
        if i not in count:
            count[i]= 1
        else:
            count[i] += 1
    return count

n = input('Enter any iterable values : ')
print(counter(n))