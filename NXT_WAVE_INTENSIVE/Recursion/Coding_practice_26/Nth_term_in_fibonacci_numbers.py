def fibonacci(n):
    if n<=1:
        return [0]
    else:
        f = [0, 1]
        for i in range(2, n):
            f.append(f[i-1] + f[i-2])
        return f

n=int(input())
print(fibonacci(n))
