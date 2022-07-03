
#!------------------------------------ !#
"""
    Name          : Tanjim Reza
    Student ID    : 20101065
    Course        : CSE422 - Artificial Intelligence
    Section       : 07
    Lab Assignment: 2

"""
#!------------------------------------ !#

import time
import random
from pprint import pprint 
# start_time = time.time()
with open('input.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')
    batsman = int(data[0].split(',')[0].split(' ')[0])
    target = int(data[0].split(',')[0].split(' ')[1])
    data.pop(0)
    runs = [ int(i.split(' ')[1]) for i in data ]
    batsman_names = [ i.split(' ')[0] for i in data ]


def fitness(model, target):
    score = 0  
    for i in range(len(model)):
        if model[i] == 1:
            score += runs[i]
    # print("(f) M_Score:",score)
    fit = score - target
    
    if fit == 0: 
        return 20101065
    else: 
        return abs(fit)

def target_found(model):
    if fitness(model, target) == 20101065:
        return True
    else:
        return False    

def mutate(model):
    index = random.randint(0, len(model)-1)
    model[index] = 1 - model[index]
    # print("Mutation Point:", index)
    return model

def crossover(model1, model2):
    index = random.randint(0, len(model1)-1)
    new_model_one = model1[:index] + model2[index:]
    new_model_two = model2[:index] + model1[index:]
    return new_model_one, new_model_two


def generate_model(batsman):
    new_model = []
    for i in range(batsman):
        new_model.append(
            random.randint(0,1)
        )
    return new_model 

population_count = 1000
population = []
iteration = 1000

for i in range(population_count):
    population.append(
        generate_model(batsman)
    ) 


# model = [1,0,1,0,1,1,1,0]
# population.append(model)
print("Population:", len(population))
print("Iterations:", iteration)
# print("--->>> START <<<---")
# pprint(population)
DO_WE_ITERATE = True
SOLUTION_FOUND = False
SOLUTION_MODEL = None
for i in range(iteration):
    for model in population:
        # print("Model:",model)
        fitness_of_current_model = fitness(model, target)
        # print("Fitness of current model:", round(fitness_of_current_model,6))
        #sort the population based on fitness
        
        if target_found(model): #! IF TARGET IS FOUND
            # print("------------------")
            # print(f"SOLUTION MODEL: {model}")
            # print("------------------")
            DO_WE_ITERATE = False
            SOLUTION_FOUND = True
            SOLUTION_MODEL = model
            break
    if DO_WE_ITERATE:
        new_population = []
        #! SORTING THE POPULATION BASED ON FITNESS
        population.sort(key=lambda x: fitness(x, target), reverse=True)
        for i in range(population_count):
            offspring_1, offspring_2 = crossover(population[0], population[1])
            #! MUTATION PROBABILITY 50%
            probability = random.randint(0,1)
            if probability == 1:
                offspring_1 = mutate(offspring_1)
                offspring_2 = mutate(offspring_2)
            new_population.append(offspring_1)
            new_population.append(offspring_2)
        population = new_population
    if DO_WE_ITERATE == False:
        break
# print("->>>> OUT OF LOOP <<<<<-")

if SOLUTION_FOUND: 
    print("All Batsman:",batsman_names)
    print("Solution Model: ", SOLUTION_MODEL)
    #batsman name from solution model 
    batsman_name = []
    for i in range(len(SOLUTION_MODEL)): 
        if SOLUTION_MODEL[i] == 1:
            batsman_name.append(batsman_names[i])
                
    print("Selected Batsman", batsman_name)
else: 
    print("-1")

# end_time = time.time()
# print("(t) Runtime:", end_time - start_time)