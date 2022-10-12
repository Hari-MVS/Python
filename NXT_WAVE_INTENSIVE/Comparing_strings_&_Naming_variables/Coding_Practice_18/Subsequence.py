m =input()
n =input()
count,j=0,0
if(len(m)==0):
    print("Yes")
if(len(n)==0):
    print("No")
        
for i in range(0,len(n)):
    while (j<len(m)):
        if (n[i] == m[j]):
            count+=1
            j+=1
            break
        j+=1
print("Yes" if count==len(n) else "No")
