a= int(input())
n=0.0
if (a<=50):
    n=(a*2)
elif (a>50 and a<=150):
    n=(50*2) +(a-50)*3
elif (a>150 and a<=250):
    n=(50*2) +(100*3)+(a-150)*5
elif (a>=250):
    n=(50*2) +(100*3)+(100*5)+(a-250)*8
print(n+(n/100)*20)
