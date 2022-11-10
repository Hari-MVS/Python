
re=''
vl={}
for i in range(2):
    for i in range(int(input()))  :
        tem =[int(i) for i in input().split()]
        if tem[0] not in vl:
            vl[tem[0]]=tem[1]
        else:
            vl[tem[0]]+=tem[1]
    
el=[(i,j) for i,j in sorted(vl.items())]

for m in sorted(el):  
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
            re=' - '+f'x'+re
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
