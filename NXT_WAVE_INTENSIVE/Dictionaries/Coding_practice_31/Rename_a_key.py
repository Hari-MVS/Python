fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

a=input()
b=input()

re=[]
for i,j in fruits.items():
    if i==a:
        re.append((b,j))
    else:
        re.append((i,j))
print(re)
