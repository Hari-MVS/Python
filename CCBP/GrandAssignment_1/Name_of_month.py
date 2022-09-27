a=int(input())
b=["January","February","March","April","May","June","July",
"August","September","October","November","December"]

if a>0 and a<=12:
    print(b[a-1])
else:
    print("Invalid Month Number")
