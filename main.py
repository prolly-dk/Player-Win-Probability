import numpy as np
import pandas as pd

from functions import *

# Parameters
playerHP, enemyHP = 50, 100
playerDmgDice, enemyDmg = 6, 5

D20_Test = Main_Simulation(playerHP, enemyHP, playerDmgDice, enemyDmg)
D20_Test = D20_Test.set_index("run")

print(D20_Test)