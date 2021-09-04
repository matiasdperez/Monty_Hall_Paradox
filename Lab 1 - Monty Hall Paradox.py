#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%
# Original arrangement

np.random.seed(42)

sim = range(10, 1000, 20)  #Number of simulations/games

results = np.zeros([len(sim),2])

for j in range(0,len(sim)):
    
    orig = np.argsort(np.random.rand(sim[j],3))==0    #Creates an boolean mx3 array representing the arrangement of cars and goats
    orig = orig.astype(int)     #Converting booleans into 0,1

    # %%
    # Contestant's choice

    choice = np.argsort(np.random.rand(sim[j],3))==0    #Creates an boolean mx3 array representing the arrangement of cars and goats
    choice = choice.astype(float)     #Converting booleans into 0,1

    # %%
    # Monty's choice after contestant

    monty = orig + choice

    for i in range(sim[j]):
        if np.max(monty[i])==1:
            monty[i, np.argmin(monty[i])] = np.nan
        else:
            monty[i, np.random.choice(np.ravel(np.argwhere(monty[i]==0)))] = np.nan

    # %%
    # Probability of winning not changing the door

    prob = np.mean(np.any(monty == 2, axis=1))

    print(sim[j], prob)

    results[j,0] = sim[j]
    results[j,1] = prob