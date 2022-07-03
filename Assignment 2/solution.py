# model input from text file

import random
from pprint import pprint
import re

with open('./1.txt', 'r') as f:
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
    print("(f) M_Score:",score)
    fit = score - target
    
    if fit == 0: 
        return 20101065
    else: 
        return abs(1/fit)

def do_we_continue(model):
    if fitness(model, target) == 20101065:
        return False
    else:
        return True    

def mutate(model):
    index = random.randint(0, len(model)-1)
    model[index] = 1 - model[index]
    print("Mutation Point:", index)
    return model

def crossover(model1, model2):
    index = random.randint(0, len(model1)-1)
    new_model_one = model1[:index] + model2[index:]
    new_model_two = model2[:index] + model1[index:]
    return new_model_one, new_model_two



population_count = 2
population = []
iteration = 10
def generate_model(batsman):
    new_model = []
    for i in range(batsman):
        new_model.append(
            random.randint(0,1)
        )
    return new_model    

for i in range(population_count):
    population.append(
        generate_model(batsman)
    ) 


model = [1,0,1,0,1,1,1,0]
population.append(model)
print("Population:", len(population))
print("--->>> START <<<---")
# pprint(population)
DO_WE_ITERATE = True
for i in range(iteration):
    for model in population:
        print("Model:",model)
        fitness_of_current_model = fitness(model, target)
        #fitness to 4 decimal places
        print("Fitness of current model:", round(fitness_of_current_model,6))
        #sort the population based on fitness
        
        
         
        if fitness_of_current_model == 20101065:
            print("------------------")
            print("Solution found")
            print(f"SOLUTION MODEL: {model}")
            print("------------------")
            DO_WE_ITERATE = False
            break
        else:
            print("Else")
            population.sort(key=lambda x: fitness(x, target), reverse=True)
            print("Sorted Population:")
            for model in population:
                print(f"-Model: {model}, Score: {fitness(model, target)}")
            print("END: Sorted Population:")
            
            offspring_1, offspring_2 = crossover(population[0], population[1])
            
            
            # crossover_model = crossover(model, population[random.randint(0, len(population)-1)])
            # model = mutate(model)
            # population.append(model)
            # population.sort(reverse=True)
            # population.pop()
            # print("Population:", len(population))
            # pprint(population)
            # print("\n")
            continue
    if DO_WE_ITERATE == False:
        break
print("->>>> OUT OF LOOP <<<<<-")
# fits = fitness(model, target)
# print("Fitness:", fits)
# mutation = mutate(model)
# print("Mutation:", mutation)

