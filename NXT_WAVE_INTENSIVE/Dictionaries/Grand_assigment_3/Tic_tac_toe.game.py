A=[]
for i in range(3):
    A.append(input().split())
for i in range(len(A)):
    
    if ((A[i][0] == "O" and A[i][1] == "O" and A[i][2] == "O") or (A[0][i] == "O" and A[1][i] == "O" and A[2][i] == "O")):
        print("Abhinav Wins")
        break
    elif ((A[i][0] == "X" and A[i][1] == "X" and A[i][2] == "X") or (A[0][i] == "X" and A[1][i] == "X" and A[2][i] == "X")):
        print("Anjali Wins")
        break
    elif (A[0][0] == 'X' and A[1][1] == 'X' and A[2][2] == 'X') or (A[0][2] =='X' and A[1][1]== 'X' and A[2][0] =='X'):
        print('Anjali Wins')
        break
    elif (A[0][0] == 'O' and A[1][1] == 'O' and A[2][2] == 'O') or (A[0][2] =='O' and A[1][1]== 'O' and A[2][0] =='O'):
        print('Abhinav Wins')
        break
else:
    print('Tie')
