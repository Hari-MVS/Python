a=input().split()
vow=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    re=''
    for j in range(len(i)):
        if i[j] in vow:
            re=i[j:]+re
            break
        else:
            re+=i[j]
    print(re,end=' ')
