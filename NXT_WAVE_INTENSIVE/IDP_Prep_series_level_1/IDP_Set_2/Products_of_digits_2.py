n=input()
for i in range(len(n)):
    if n[i]=='0':
        continue
    else:
        n=n[i:]
        break

pro=1
for i in n:
    pro*=int(i)
print(pro)
