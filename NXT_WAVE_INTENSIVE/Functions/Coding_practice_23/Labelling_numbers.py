def show_numbers(number):
    if number%2==0:
        return str(number)+" EVEN"
    else:
        return str(number)+" ODD"
        


number = int(input())
for i in range(number+1):
    print(show_numbers(i))
