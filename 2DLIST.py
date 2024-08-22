matrix=[[1,3],[5,6],[4,1]]
print(matrix)
#Number Of Rows
print(len(matrix))

#Number of Columns
print(len(matrix[0]))

print(matrix[1][0])


matrix1=[[3,4,5],[7,8,9],[1,2,3],]

#Number of Rows
print(len(matrix1))

#Number of Columns
print(len(matrix1[1]))

print(matrix1[0][0])


for row in range(0,len(matrix1)):
    for column in range(0,len(matrix1[1])):
        print(matrix1[row][column], end=" ")
    print("\n")


rows=int(input("Enter the number of rows."))
columns=int(input("Enter the number of columns."))
a=[]
for row in range(rows):
    temp=[]
    for column in range(columns):
        h=int(input("Enter your elements"))
        temp.append(h)
    a.append(temp)
for row in range(rows):
    for column in range(columns):
        print(a[row][column], end=" ")
    print("\n")


b=[]
for row in range(rows):
    for column in range(columns):
        h=int(input("Enter your elements"))
        b.append(h)
for row in range(rows):
    for column in range(columns):
        print(b[row][column])