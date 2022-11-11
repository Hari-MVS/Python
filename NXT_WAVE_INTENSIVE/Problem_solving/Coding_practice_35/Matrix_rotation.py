def get_rotation(matrix,times_of_rotation):
    l=len(matrix)
    #print("r:{}".format(times_of_rotation))
    for i in range(times_of_rotation):
        new_matrix=[]
        for j in range(l):
            row=[]
            for k in range(l):
                row.append(matrix[k][j])
            new_matrix.append(row[::-1])
        matrix=new_matrix
    
    return matrix
    
    
def get_update(matrix,index_value1,index_value2,new_value):
    matrix[index_value1][index_value2]=new_value
    #matrix=get_rotation(matrix,times_of_rotation)
    return matrix


n=int(input())
matrix=[]
a_u_r=0
for i in range(n):
    matrix.append(input().split())
matrix_copy=matrix.copy()
while True:
    op=input().split()
    if op[0] == "-1":
        break
    #matrix=get_decide_op(op,matrix)
    if op[0] == "R":
        #print(op[0],op[1])
        angle=op[1]
        times_of_rotation=int(angle)//90
        a_u_r+=times_of_rotation
        matrix=get_rotation(matrix,times_of_rotation)
        #print(after_op)
    elif op[0] == "Q" :
        #print(op[0],op[1],op[2])
        i,j=int(op[1]),int(op[2])
        print(matrix[i][j])
    elif op[0] == "U":
        #print(op[0],op[1],op[2],op[3])
        index_value1,index_value2=int(op[1]),int(op[2])
        new_value=op[3]
        matrix=get_update(matrix_copy,index_value1,index_value2,new_value)
        #print(a_u_r)
        #print(matrix)
        matrix=get_rotation(matrix,a_u_r)
        #print(matrix)
