from datetime import datetime

m=datetime.strptime(input(),'%b %d %Y %I:%M%p')
print(datetime.strftime(m,'%d/%m/%Y %H:%M:%S'))
