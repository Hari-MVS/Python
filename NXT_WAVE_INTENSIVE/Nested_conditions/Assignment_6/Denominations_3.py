num= int(input())

f=num//500
num%=500
b=num//50
num %=50
h=num//10
num%=10
g=num//1
print(f'500: {f} 50: {b} 10: {h} 1: {g}')
