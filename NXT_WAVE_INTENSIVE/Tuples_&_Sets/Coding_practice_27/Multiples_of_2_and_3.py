n=int(input())
m2=()
m3=()
for i in range(1,n+1):
    m2+=(2*i,)
    m3+=(3*i,)

print(sorted([i for i in m2 if i%3!=0]))

print(sorted([i for i in m3 if i not in m2]+[i for i in m2 if i%3!=0]))
        
