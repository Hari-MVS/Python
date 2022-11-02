alpha=[chr(i) for i in range(97,123)]

for i in input().split():
    print(alpha[int(i)-1],end='')
