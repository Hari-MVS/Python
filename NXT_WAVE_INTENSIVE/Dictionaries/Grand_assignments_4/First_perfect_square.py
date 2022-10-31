n=int(input())
m=int(input())
for i in range(m):
    if i*i in range(n,m+1):
        print(i*i)
        break
else:
    print('No Perfect Square')
        
    
