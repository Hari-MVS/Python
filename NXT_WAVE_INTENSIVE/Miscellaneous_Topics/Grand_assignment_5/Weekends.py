import datetime

fir= datetime.datetime.strptime(input(),'%d %b %Y')
las= datetime.datetime.strptime(input(),'%d %b %Y')
dif=str(las-fir).split()[0]
sat=0
sun=0
for i in range(int(dif)+1):
    tem=fir+datetime.timedelta(i)
    
    if tem.strftime('%A') == 'Saturday':
        sat+=1
    elif tem.strftime('%A') == 'Sunday':
        sun+=1
print('Saturday:',sat)
print('Sunday:',sun)
