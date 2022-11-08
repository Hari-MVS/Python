import datetime
cur = datetime.datetime.strptime(input(),'%b %d %Y')
print(cur+ datetime.timedelta(days=365*int(input())))

