n= int(input())
year =(n//365)
print(year)
week = n-year*365 
print(week//7)
print(week - (week//7)*7)
