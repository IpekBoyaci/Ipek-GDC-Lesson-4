rainbow=["red","orange","yellow","green","blue","darkblue","purple"]

print(rainbow[3])
print(rainbow[-1])
print(len(rainbow))

#append function will help to add new values to the list
rainbow.append("violet")
print(rainbow)

#insert function will help to add a value to the list in a specific position

rainbow.insert(3,"white")
print(rainbow)

#pop function will help to remove a value from a list
#if you use pop alone it will remove the last value from the list

rainbow.pop()
print(rainbow)

#if you give the index value after pop it will remove that value in particular

rainbow.pop(3)
print(rainbow)

#2D list are lists with small lists in them
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

#To get the number of rows in a list we will use len(matrix)

print(len(matrix))

#To get the number of columns we will use len(matrix[0]) to find the number of values in the first list which will give the column

print(len(matrix[0]))

#
print(matrix[2][0])

print(matrix[-1][-1])

#Printing Matrix in Matrix form:
#Loop through the row
#Loop through the column
#Print the element of a row
#Print new line

for i in range(3):
    for j in range(3):
        print(matrix[i][j],end=" ")
    print("\n")
    