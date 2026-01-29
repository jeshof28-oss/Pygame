matrix = [[1, 2, 3],[4,5,6],[7,8,9]]
print(matrix)
print(len(matrix))
print(len(matrix[0]))
for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        print(matrix[i][j], end=" ")
    print("\n")

rows=int(input("Enter the number of rows and columns- "))
col=rows

Matrix = []

for i in range(rows):
    temp=[]
    for j in range(col):
        val = int(input("Enter the value - "))
        temp.append(val)
    Matrix.append(temp)

for i in range(0, len(Matrix)):
    for j in range(0, len(Matrix)):
        print(Matrix[i][j], end=" ")
    print("\n")

#HW: Make sqaure matrix (same row and col)