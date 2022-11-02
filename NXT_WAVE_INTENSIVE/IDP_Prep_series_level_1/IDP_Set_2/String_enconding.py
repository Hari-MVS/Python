alpha=[chr(i) for i in range(97,123)]
a=input()
b=input()
re=''
ele_dia=[]
le=len(alpha)-1
for i in range(len(a)):
    tem=alpha.index(a[i])
    tem2=alpha.index(b[i])
    dif=abs(alpha.index(b[i])-alpha.index(a[i]))
    if tem+dif==tem2 and tem+dif <=le:
        ele_dia.append(dif)
        re+=b[i]
    else :
        dif=(le-tem)+tem2+1
        ele_dia.append(dif)
        re+=b[i]
print('Yes' if re==b and len(set(ele_dia))==1 else 'No')
    

