strings=[input() for i in range(3)]
t=[int(i) for i in input()]

re=''
for i in t:
    re+=strings[i-1]
print(re)
