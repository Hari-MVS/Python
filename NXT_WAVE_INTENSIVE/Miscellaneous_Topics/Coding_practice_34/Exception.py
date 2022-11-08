a,b=input().split()

try: 
    c = int(a)/int(b)
    print(c)  
except ZeroDivisionError:  
    print("Denominator can't be 0")
except ValueError:
    print('Input should be an integer')
