m,n=input().split()
matrix=[]
for i in range(int(m)):
    matrix.append([int(i) for i in input().split()])

total = int(m) + int(n) - 2
for i in range(total+1):
    for j in range(i+1):
        if j < int(m) and i - j < int(n):
            print(matrix[j][i - j], end=" ")
    print()
