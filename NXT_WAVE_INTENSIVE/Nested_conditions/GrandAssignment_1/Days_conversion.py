n= int(input())
year =(n//365)
print(year,'years',end=' ')
week = n-year*365 
print(week//7,'weeks',end=' ')
print(week - (week//7)*7,'days')
