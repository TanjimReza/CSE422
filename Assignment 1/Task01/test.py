input = []
with open("input.txt") as textFile:
    for line in textFile:
        inputs= [item.strip() for item in line.split()]
        input.append(inputs)

columnCount = len(input[0])
rowCount = len(input)
temporary = 0


visited = []
for i in range(rowCount):
   visited.append([0 for j in range(columnCount)])



def dfs(row,column):
    global temporary
    temporary += 1
    visited[row][column] = 1

    if column<columnCount and column>=0 and row-1<rowCount and row-1>=0 and visited[row-1][column] == 0 and input[row-1][column] == 'Y':
        dfs(row-1,column)  # up
    if column+1<columnCount and column+1>=0 and row<rowCount and row>=0 and visited[row][column+1] == 0 and input[row][column+1] == 'Y':
        dfs(row, column+1)  # right
    if column<columnCount and column>=0 and row+1<rowCount and row+1>=0 and visited[row+1][column] == 0 and input[row+1][column] == 'Y':
        dfs(row+1, column)  # down
    if column-1<columnCount and column-1>=0 and row<rowCount and row>=0 and visited[row][column-1] == 0 and input[row][column-1] == 'Y':
        dfs(row, column-1)  # left


    if column+1<columnCount and column+1>=0 and row+1<rowCount and row+1>=0 and visited[row+1][column+1] == 0 and input[row+1][column+1] == 'Y':
        dfs(row+1, column+1)
    if column-1<columnCount and column-1>=0 and row+1<rowCount and row+1>=0 and visited[row+1][column-1] == 0 and input[row+1][column-1] == 'Y':
        dfs(row+1, column-1)
    if column+1<columnCount and column+1>=0 and row-1<rowCount and row-1>=0 and visited[row-1][column+1] == 0 and input[row-1][column+1] == 'Y':
        dfs(row-1, column+1)
    if column-1<columnCount and column-1>=0 and row-1<rowCount and row-1>=0 and visited[row-1][column-1] == 0 and input[row-1][column-1] == 'Y':
        dfs(row-1, column-1)



max_value = []
for a in range(rowCount):
    for b in range(columnCount):
        if visited[a][b] == 0 and input[a][b] == 'Y':
            temporary = 0
            dfs(a,b)
            max_value.append(temporary)

temp=0
for i in range(len(max_value)):
    if temp<max_value[i]:
        temp= max_value[i]
print(temp)
