
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

#####? TASK 01: USING DFS ######

#! Creating a 2D Matrix from 'input.txt'
matrix = []
with open('input.txt', 'r') as inputFile:
    data = inputFile.readlines() #?> Reading Each Line 
    for line in data:
        matrix.append(line.split()) #?> Adding every line to the matrix
pprint(matrix)
print("\n")    

max_count = 0 #*> Using a Global Variable to store the max count
result = 0 

#! Created A Function to check if the possible movements are valid or not 
def is_row_col_valid(matrix, row, col):
    """A function to check if the possible movements are valid for my operation

    Args:
        matrix (list): Main Matrix to be operated on
        row (int): row index of the matrix
        col (int): column index of the matrix

    Returns:
        int: Returns True if the movement is valid else False
    """    
    if row < 0 or col < 0 or row >= len(matrix)-1 or col >= len(matrix[row])-1 or matrix[row][col] == 'N':
        #?> Basic: If the row, col is out of range or the position is N, then already visited or not valid. 
        return False
    return True


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
    if is_row_col_valid(matrix, row, col):
        matrix[row][col] = "N"
        if matrix[row][col] == "Y": #?> Current
            max_count += 1
        if matrix[row+1][col] == "Y": #?> Bottom 
            max_count += 1
        if matrix[row+1][col+1] == "Y": #?> Diagonal Bottom Right
            max_count += 1 
        if matrix[row+1][col-1] == "Y": #?> Diagonal Bottom Left    
            max_count += 1

    return max_count

def start_search(matrix):
    global result #*> Using a Global Variable to store final result
    current_result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])): 
            # print(row,col) #!Got Each item
            current_result = search_neighbour_positions(matrix, row, col)
            result = max(result,current_result) #?> Storing the max between the current result and the previous result
    return result

task01_result = start_search(matrix)
print("Task 01: ", task01_result)
#?-----------------------------?#









