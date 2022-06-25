
#!------------------------------------ !#
"""
    Name          : Tanjim Reza
    Student ID    : 20101065
    Course        : CSE422 - Artificial Intelligence
    Section       : 07
    Lab Assignment: 1

"""
#!------------------------------------ !#

""" Task01 Analogy:
    
    1. In Every Step, I need to check the positions for Y and N. 
    If Y connects with another Y in any direction, then I need to add 1 to the result and start searching from the connected Y.
    
    2. For every DFS, I could have added another MATRIX to check if the position is visited or not,
    But changing the position of the Y to N, I could have made the same result without using extra more space.
    
    All the imports, print, pprint statements are for debugging & visualization purpose.

"""
#*----------------*#  
#* Global Imports *#
from pprint import pprint
#*----------------*# 
#* Global Variables *#
max_count = 0 #*> Using a Global Variable to store the max count
result = 0 
#####? TASK 01: USING DFS ######

#! Creating a 2D Matrix from 'input.txt'
matrix = []
with open('input.txt', 'r') as inputFile:
    data = inputFile.readlines() #?> Reading Each Line 
    for line in data:
        matrix.append(line.split()) #?> Adding every line to the matrix

print("\n")    

# visited = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
# pprint(visited)

# #! Created A Function to check if the possible movements are valid or not 
# def is_row_col_valid(matrix, row, col):
#     """A function to check if the possible movements are valid for my operation

#     Args:
#         matrix (list): Main Matrix to be operated on
#         row (int): row index of the matrix
#         col (int): column index of the matrix

#     Returns:
#         int: Returns True if the movement is valid else False
#     """    
#     # if row < 0 or col < 0 or row >= len(matrix)-1 or col >= len(matrix[row])-1 or matrix[row][col] == 'N':
#     #     #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
#     #     return False
#     print(len(matrix[0]))
#     if col < len(matrix[0]) and col >= 0 and row < len(matrix) and row >= 0 and matrix[row][col] == 'Y':
#         #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
#         return True
    
#     return True


def search_neighbour_positions(matrix, row, col):
    """Search all other possible movements for the current position.
    Args:
        matrix (list): _description_
        row (int): row index of the matrix
        col (int): column index of the matrix

    Returns:
        int: max count of the possible movements
    """    
    global max_count #*> Using a Global Variable to store the max count
    print("MAX:", max_count)
    max_count += 1
    #!UP 
    if row-1> 0 and col < len(matrix[0]) and col >= 0 and row-1 >= 0 and \
        matrix[row-1][col] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row-1][col] = 'N'
        search_neighbour_positions(matrix, row-1, col)
    
    #!DOWN

    if row+1 < len(matrix) and col < len(matrix[0]) and col >= 0 and row+1 >= 0 and\
        matrix[row+1][col] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row+1][col] = 'N'
        search_neighbour_positions(matrix, row+1, col)
    
    #!LEFT
    if col-1 >= 0 and row < len(matrix) and row >= 0 and col-1 < len(matrix[0]) and \
        matrix[row][col-1] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row][col-1] = 'N'
        search_neighbour_positions(matrix, row, col-1)
    
    #!RIGHT
    if col+1 < len(matrix[0]) and row < len(matrix) and row >= 0 and \
        matrix[row][col+1] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row][col+1] = 'N'
        search_neighbour_positions(matrix, row, col+1)
      
    #!UP-LEFT
    if row-1> 0 and col-1 >= 0 and col-1 < len(matrix[0]) and row-1 < len(matrix) and \
        matrix[row-1][col-1] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row-1][col-1] = 'N'
        search_neighbour_positions(matrix, row-1, col-1)
    #!UP-RIGHT
    if row-1> 0 and col+1 < len(matrix[0]) and col+1 >= 0 and row-1 < len(matrix) and \
        matrix[row-1][col+1] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row-1][col+1] = 'N'
        search_neighbour_positions(matrix, row-1, col+1)
    
    #!DOWN-LEFT
    if row+1 < len(matrix) and col-1 >= 0 and col-1 < len(matrix[0]) and row+1 < len(matrix) and \
        matrix[row+1][col-1] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row+1][col-1] = 'N'
        search_neighbour_positions(matrix, row+1, col-1)
        
    #!DOWN-RIGHT
    if row+1 < len(matrix) and col+1 < len(matrix[0]) and col+1 >= 0 and row+1 < len(matrix) and \
        matrix[row+1][col+1] == 'Y':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        matrix[row+1][col+1] = 'N'
        search_neighbour_positions(matrix, row+1, col+1)
    return max_count

    
    
    # # if is_row_col_valid(matrix, row, col):
    # #     matrix[row][col] = "N"
    # #     if matrix[row][col] == "Y": #?> Current
    # #         max_count += 1
    # #     if matrix[row+1][col] == "Y": #?> Bottom 
    # #         max_count += 1
    # #     if matrix[row+1][col+1] == "Y": #?> Diagonal Bottom Right
    # #         max_count += 1 
    # #     if matrix[row+1][col-1] == "Y": #?> Diagonal Bottom Left    
    # #         max_count += 1
 
    # return max_count
 
def start_search(matrix):
    global result #*> Using a Global Variable to store final result
    current_result = 0
    global max_count #*> Using a Global Variable to store the max count
    for row in range(len(matrix)):
        for col in range(len(matrix[row])): 
            # print(row,col) #!Got Each item
            if matrix[row][col] == "Y":
                current_result = 0
                print("Current Result: ", current_result)
                # result = max(search_neighbour_positions(matrix, row, col),result)
                current_result = search_neighbour_positions(matrix, row, col)
                max_count = 0
                result = max(current_result, result)
                
    return result-1

task01_result = start_search(matrix)
print("Task 01: ", task01_result)
with open("task01.txt", "w") as f:
    f.write(str(task01_result))
    f.close()
#?-----------------------------?#
