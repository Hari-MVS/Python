def calculate_bill(amount):
    return amount-(amount*5)/100 if amount<500 else amount-(amount*10)/100 if amount>=500 and amount<2500 else amount-(amount*20)/100


amount = int(input())
print(round(calculate_bill(amount),3))
