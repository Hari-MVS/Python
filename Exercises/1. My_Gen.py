def my_gen(n):
    i = 0
    while i < n:
        if i % 2 == 0:
            yield i 
        i = i +1
        
iterates = my_gen(int(input('Enter any number : ')))
print(next(iterates))
print(next(iterates))
print(next(iterates))
print(next(iterates))
print(next(iterates))
print(next(iterates))


