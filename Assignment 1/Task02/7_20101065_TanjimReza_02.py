from pprint import pprint
matrix = []
with open('input2.txt', 'r') as inputFile:
    max_row = int(inputFile.readline())
    max_column = int(inputFile.readline())
    data = inputFile.readlines() #?> Reading Each Line 
    for line in data:
        matrix.append(line.split()) #?> Adding every line to the matrix


# print("\n")  
# pprint(matrix)
# print("Column:", max_column)
# print("Row:", max_row)
visited = [[0 for i in range(int(max_column))] for j in range(int(max_row))]


count = 0 
allHumans = 0
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'H':
            allHumans += 1

# print("All Humans:", allHumans)
def bfs(matrix):
    global allHumans
    queue = []
    for i in range(int(max_row)):
        for j in range(int(max_column)):
            if matrix[i][j] == 'A':
                queue.append([i,j])
    while queue:
        # print(queue)
        row, col = queue.pop(0)
        row = int(row)
        col = int(col)
        # print(row,col)
        # print(type(row), type(col))
        if col < max_column and col >= 0 and row-1 < max_row and row-1 >= 0 and matrix[row-1][col] == 'H':
            matrix[row-1][col] = 'N'
            queue.append([row-1,col])
            visited[row-1][col] = visited[row][col] + 1
            allHumans -= 1

        if col+1 < max_column and col+1 >= 0 and row < max_row and row >= 0 and matrix[row][col+1] == 'H':
            matrix[row][col+1] = 'N'
            queue.append([row,col+1])
            # print(type(row), type(col))
            visited[row][col+1] = visited[row][col] + 1 
            allHumans -= 1
        if col-1 < max_column and col-1 >= 0 and row < max_row and row >= 0 and matrix[row][col-1] == 'H':
            matrix[row][col-1] = 'N'
            queue.append([row,col-1])
            visited[row][col-1] = visited[row][col] + 1 
            allHumans -= 1
        if row+1 < max_row and row+1 >= 0 and col < max_column and col >= 0 and matrix[row+1][col] == 'H':
            matrix[row+1][col] = 'N'
            queue.append([row+1,col])
            visited[row+1][col] = visited[row][col] + 1 
            allHumans -= 1  
    
    max_value = 0   
    for i in range(int(max_row)):
        for j in range(int(max_column)):
            if visited[i][j] > max_value:
                max_value = visited[i][j]
    return allHumans, max_value
         
output = ""
output += f"Time: {bfs(matrix)[1]} minutes\n"
if bfs(matrix)[0] == 0:
    output += "No one survived"
else: 
    output += f"{bfs(matrix)[0]} survived"

print(output)
