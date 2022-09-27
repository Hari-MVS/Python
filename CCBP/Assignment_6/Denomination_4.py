num= int(input())
e=num//2000
num%=2000
f=num//500
num%=500
a= num//200
num %=200
b=num//50
num %=50
h=num//20
num%=20
c=num//5
num %=5
d=num//2
num%=2
g=num//1
print(f'2000:{e} 500:{f} 200:{a} 50:{b} 20:{h} 5:{c} 2:{d} 1:{g}')
