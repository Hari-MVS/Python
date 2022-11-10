n=int(input())
re=''
vl=[]
for i in range(n)  :
    temp=()
    for j in input().split():
        temp+=(int(j),)
    vl.append(temp)

for m in sorted(vl):  
    if abs(m[0])==0 and abs(m[1]) ==0:
        if m[0]<0:
            re=' - '+str(m[0])+re
        else:
            re=' + '+str(m[0])+re
    elif abs(m[0])==0:
        if m[1]<0:
            re=' - '+str(abs(m[1]))+re
        else:
            re=' + '+str(abs(m[1]))+re
    elif abs(m[1])==0:
        continue
    elif abs(m[0]) == 1:
        if m[1]<0:
            re=' - '+f'{abs(m[1])}x'+re
        else:
            re=' + '+f'{m[1]}x'+re
    elif abs(m[1])==1:
        if m[1]<0:
            re=' - '+f'x^{abs(m[0])}'+re
        else:
            re=' + '+f'x^{m[0]}'+re
    else:
        if (abs(m[1])> abs(m[0]) and m[1]<0) or (abs(m[0])> abs(m[1]) and m[0]<0):
            re=' - '+f'{abs(m[1])}x^{abs(m[0])}'+re
        else:
            re=' + '+f'{abs(m[1])}x^{abs(m[0])}'+re
print(re[3:] if re[1]=='+' else re[1]+re[3:])
# print(re.split('+') if re[1]=='+' else re.split('-'))
        
