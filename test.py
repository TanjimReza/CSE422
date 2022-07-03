
def fitness(model, target):
    score = model  
    print("M_Score:",score)
    fit = score - target
    
    if fit == 0: 
        return 20101065
    else: 
        return abs(target/fit)
target = 1001
model = 
print(fitness(model, target))