import numpy as np
import pandas as pd

from functions import *

# Parameters
playerHP, enemyHP = 50, 100
playerDmgDice, playerDiceNum, enemyDmg = 6, 2, 5

simulation_results = Main_Simulation(playerHP, enemyHP, playerDmgDice, enemyDmg, playerDiceNum)
simulation_results = simulation_results.set_index("run")