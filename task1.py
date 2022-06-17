
#* Imports *#
from pprint import pprint
#*---------*#


#? CREATE 2D Matrix from InputFile
matrix = []
with open('input.txt', 'r') as f:
    data = f.readlines()
    for line in data: 
        matrix.append(line.split())
pprint(matrix)
print("\n")    
#? ------------------------------- #? 

def search_for_infected_neighbours(matrix, row, column):
    if row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[row]):
        return 0
    if matrix[row][column] == 'N':
        return 0
    maximum = 1 
    matrix[row][column] = 'N'
    pprint(matrix)
    for currentRow in range(row-1,row+2):
        for currentColumn in range(column-1,column+2):
            if currentRow != row or currentColumn != column:
                print("We got One Infection, Operation Findlight")
                maximum += search_for_infected_neighbours(matrix, currentRow, currentColumn)
    return maximum


def get_maximum_connected_region(matrix):
    maxregion = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 'Y':
                # print(f"{row, column}:",matrix[row][column])
                # print("We got One Infection, Operation Findlight")
                result = search_for_infected_neighbours(matrix, row, column)
                print(result)
                maxregion = max(maxregion, result)
    return maxregion
final = get_maximum_connected_region(matrix)
print("FINAL:",final)