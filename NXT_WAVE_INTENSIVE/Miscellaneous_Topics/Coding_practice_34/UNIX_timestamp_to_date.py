import datetime
n=int(input())
print(datetime.datetime.fromtimestamp(n).strftime('%Y-%m-%d %H:%M:%S'))
