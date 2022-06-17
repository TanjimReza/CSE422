#* Imports *#
from pprint import pprint
#*---------*#
#ADDED THIS LINE HERE
#? CREATE 2D Matrix from InputFile
matrix = []
with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        matrix.append(line.split())
pprint(matrix)
print("\n")    

visited = matrix
max_count = 0 
 
def isvalid(matrix, row, col):
    if row < 0 or col < 0 or row >= len(matrix)-1 or col >= len(matrix[row])-1 or matrix[row][col] == 'N':
        return False
    return True

def search_neighbours(matrix, row, col):
    global max_count
    if isvalid(matrix, row, col):
        matrix[row][col] = "N"
        if matrix[row][col] == "Y":
            max_count += 1
            print("Y on:",row,col) 
        if matrix[row+1][col] == "Y": 
            max_count += 1
            print("Y on:",row+1,col) 
        if matrix[row+1][col+1] == "Y": #?Diagonal Bottom Right
            max_count += 1
            print("Y on:",row+1,col+1) 
        if matrix[row+1][col-1] == "Y": #?Diagonal Bottom Left    
            max_count += 1
            print("Y on:",row+1,col-1)     
    return max_count

result = 0 
def start_search(matrix):
    global result
    current_result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])): 
            # print(row,col) #!Got Each item
            current_result = search_neighbours(matrix, row, col)
            result = max(result,current_result)
    return result

print(start_search(matrix))
pprint(matrix)