def get_discount(amount):
    return "5%" if amount<500 else "10%" if amount>=500 and amount<2500 else "20%"


amount = int(input())
print(get_discount(amount))
