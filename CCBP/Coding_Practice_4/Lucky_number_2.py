a=int(input())
print("Number is divisible by 6" if a%6==0 else ("Number is divisible by 3"
if a%3==0 else ("Number is divisible by 2" 
if a%2==0 else "Number is not divisible by 2, 3 or 6")))
