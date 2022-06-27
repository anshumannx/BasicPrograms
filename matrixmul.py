rows = int(input())
columns = int(input())
mat = []
for i in range(0,rows) :
    r=[]
    for j in range(0,columns) :
        r.append(int(input()))
    mat.append(r)
for i in range(0,rows) :
    for k in range (0,columns) :
        print(mat[i][k],end=" ")
    print(" ")
mat2 = []
for i in range(0,rows) :
    a = []
    for j in range(0,columns) :
        a.append(int(input()))
    mat2.append(a)
for i in range(0,rows) :
    for j in range(0,columns) :
        print(mat2[i][j],end=" ")
    print(" ")
mat3 = []
for i in range (0,rows) :
    for j in range(0,columns) :
        for k in range(0,columns) :
            mat3[i][j] +=mat[i][j]*mat2[i][j]
for i in range(0,rows) :
    for j in range(0,columns) :
        print(mat3[i][j],end=" ")
    print(" ")