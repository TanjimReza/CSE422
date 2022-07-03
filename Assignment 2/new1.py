input = []

import random
from sys import exit
from pprint import pprint

with open("1.txt") as textFile:

    for line in textFile:
        inputs = [item.strip() for item in line.split()]
        input.append(inputs)
a = int(input.pop(0)[0])

pprint(input)
populationCount = 1000
iteration = 1000 

def genNew():
    temporary = []
    for j in range(a):
        current=random.randint(0, 1)
        temporary.append(current)
    return temporary


newPopulation = []
for i in range(populationCount):
    cur = genNew()
    while(1 in cur == False):
        cur = genNew()
    newPopulation.append(cur)

print(newPopulation)

def fitnessFunction(human):
    fitnessValue = 0
    for j in range(a):
        if human[j] == 1:
           if input[j][0] == 'd':
              fitnessValue = fitnessValue - int(input[j][1])
           else:
              fitnessValue = fitnessValue + int(input[j][1])

    b = abs(fitnessValue)
    return b


def sortByFitness():
    for i in range(populationCount):
        for j in range(i+1, populationCount, 1):
            if fitnessFunction(newPopulation[i]) > fitnessFunction(newPopulation[j]):
                temporary = newPopulation[i]
                newPopulation[i] = newPopulation[j]
                newPopulation[j] = temporary




def cross():
    sortByFitness()
    newPop = []
    global newPopulation
    while len(newPopulation) > 0:
        pop1 = newPopulation.pop(0)
        pop2 = newPopulation.pop(0)
        pc = random.randint(1 , a-1)
        new1 = pop1[: pc] + pop2[pc:]
        new2 = pop2[: pc] + pop1[pc:]
        mutated(new1)
        mutated(new2)
        newPop.append(new1)
        newPop.append(new2)
    newPopulation = newPop


def mutated(c):
    random1 = random.randint(0, a-1)
    if random.randint(0, 1000) == 1:
        c[random1] = 1


for i in range( iteration ):
    for j in newPopulation:
        if fitnessFunction(j) == 0 and 1 in j:
            print(j)
            exit()
    cross()
print(str(-1) + " Maximum number of iterations reached, try again ")

