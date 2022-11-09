import datetime

n=input()
fir=datetime.datetime.strptime(n,'%b %d %Y %I:%M %p')
las=datetime.datetime(fir.year+1,1,1)
dif=las-fir
m=str(dif).split()
tim=m[-1].split(':')

ad=(dif.days*24)+int(tim[0])
print(f'{ad} hours {tim[1]} minutes')
