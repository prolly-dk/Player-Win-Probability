import numpy as np
import pandas as pd

from functions import *

# Parameters
playerHP, enemyHP = 50, 100
playerDmgDice, enemyDmg = 6, 5

simulation_results = Main_Simulation(playerHP, enemyHP, playerDmgDice, enemyDmg)
simulation_results = simulation_results.set_index("run")

print(simulation_results)