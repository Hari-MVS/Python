num= int(input())
e=num//1000
num%=1000
f=num//500
num%=500
a= num//100
num %=100
b=num//50
num %=50
h=num//20
num%=20
c=num//5
num %=5
g=num//1
print(f'1000:{e}') 
print(f'500:{f}') 
print(f'100:{a}')
print(f'50:{b}')
print(f'20:{h}')
print(f'5:{c}')
print(f'1:{g}')
