import datetime
cur = datetime.datetime.strptime(input(),'%b %d %Y')
last = datetime.datetime.strptime(input(),'%b %d %Y')

dif=str(last-cur).split()[0]

for i in range(int(dif)+1):
    print(cur+ datetime.timedelta(days=i))
