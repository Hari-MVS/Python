# n=[int(i) for i in list(input())]
# print(sum(n))


def sumof(n):
    if n<10:
        return n
    else:
        return (n%10)+sumof(n//10)
num=int(input())
print(sumof(num))
