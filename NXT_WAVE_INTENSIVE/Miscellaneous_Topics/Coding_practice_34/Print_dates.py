

import datetime

cur = datetime.datetime.strptime(input(),'%d %b %Y')
pr = cur - datetime.timedelta(days=1)
print (str(pr))

print (str(cur))


ne = cur + datetime.timedelta(days=1)
print (str(ne))
