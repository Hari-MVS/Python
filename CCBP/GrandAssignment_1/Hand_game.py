a=input()
b=input()
if a==b:
    print("Tie")
elif b=="Scissors" and a=="Paper":
    print("Anjali Wins")
elif b=="Rock" and a=="Scissors":
    print("Anjali Wins")
elif b=="Paper" and a=="Rock":
    print("Anjali Wins")
elif a=="Scissors" and b=="Paper":
    print("Abhinav Wins")
elif a=="Rock" and b=="Scissors":
    print("Abhinav Wins")
elif a=="Paper" and b=="Rock":
    print("Abhinav Wins")
    
