rows = int(input("Enter the number of rows :\t"))
columns = int(input("Enter the number of columns :\t"))
mat1= []
for i in range(rows):
        r = []
        for j in range(columns):
            num = int(input( "Enter the matrix \t"))
            r.append(num)
        mat1.append(r)
for it in range(rows) :
    for ti in range(columns) :
        print(mat1[it][ti],end=" ")
    print("\n")

mat2=[]
for i in range(rows) :
    r=[]
    for j in range(columns) :
        num2 = int(input("Enter values for matrix :\t"))
        r.append(num2)
    mat2.append(r)
mat3=[]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j] + mat2[i][j]
for r in mat3 :
    print(r)