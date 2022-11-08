import datetime
cur = datetime.datetime.strptime(input(),'%d %b %Y')
print(cur.strftime('%A'))

