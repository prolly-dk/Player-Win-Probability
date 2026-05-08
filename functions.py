import numpy as np
import pandas as pd

# SEED
np.random.seed(425)

# CONSTANTS
SAMPLE_SIZE = 10000
MULTIPLIER = 2

# MECHANICS
def D20Roll():
    roll = np.random.randint(low=1, high=21)
    return roll

def PlayerDamageRoll(Max):
    damage = np.random.randint(low=1, high=Max+1) + np.random.randint(low=1, high=Max+1)
    return damage;

def HPCalc(HP, Damage):
    HP = HP - Damage
    return HP

# SIMULATIONS
def Single_Simulation(
    defaultPlayerHP, defaultEnemyHP, playerDamageMax, enemyDamage
):
    playerHP, enemyHP = defaultPlayerHP, defaultEnemyHP
    playerDmg, enemyDmg = 0, enemyDamage

    roundsCount, missCount, hitCount, nat20Count, nat1Count = 0, 0, 0, 0, 0
    damagePlayerDealt, damageEnemyDealt, remainingPlayerHP, remainingEnemyHP = 0, 0, 0, 0

    while playerHP > 0 and enemyHP > 0:
        roll = D20Roll()
        roundsCount += 1

        if roll == 1:
            enemyDmgCrit = enemyDmg * MULTIPLIER
            damageEnemyDealt += enemyDmgCrit
            playerHP = HPCalc(playerHP, enemyDmgCrit)
            nat1Count += 1
            missCount += 1

        elif roll == 20:
            playerDmgCrit = PlayerDamageRoll(playerDamageMax) * MULTIPLIER
            damagePlayerDealt += playerDmgCrit
            enemyHP = HPCalc(enemyHP, playerDmgCrit)
            nat20Count += 1
            hitCount += 1

        elif roll <= 11:
            damageEnemyDealt += enemyDmg
            playerHP = HPCalc(playerHP, enemyDmg)
            missCount += 1

        elif roll >= 12:
            playerDmg = PlayerDamageRoll(playerDamageMax)
            damagePlayerDealt += playerDmg
            enemyHP = HPCalc(enemyHP, playerDmg)
            hitCount += 1
    
    remainingEnemyHP = enemyHP
    remainingPlayerHP = playerHP

    return {
        "result": "win" if enemyHP <= 0 else "loss",
        "rounds": roundsCount,
        "damage_dealt_player": damagePlayerDealt,
        "damage_dealt_enemy": damageEnemyDealt,
        "remaining_player_hp": remainingPlayerHP,
        "remaining_enemy_hp": remainingEnemyHP,
        "miss_count": missCount,
        "hit_count": hitCount,
        "nat20": nat20Count,
        "nat1": nat1Count
    }

def Main_Simulation(
        defaultPlayerHP, defaultEnemyHP, playerDamageMax, enemyDamage
):
    RunDict = []
    for run in range(SAMPLE_SIZE):
        sim_results = Single_Simulation(
            defaultPlayerHP, defaultEnemyHP, playerDamageMax, enemyDamage
        )

        RunDict.append({
            "run": run + 1,
            "result": sim_results["result"],
            "rounds": sim_results["rounds"],
            "damage_player_dealt": sim_results["damage_dealt_player"],
            "damage_enemy_dealt": sim_results["damage_dealt_enemy"],
            "remaining_player_hp": sim_results["remaining_player_hp"],
            "remaining_enemy_hp": sim_results["remaining_enemy_hp"],
            "miss_count": sim_results["miss_count"],
            "hit_count": sim_results["hit_count"],
            "nat20": sim_results["nat20"],
            "nat1": sim_results["nat1"]
        })
    
    return pd.DataFrame(RunDict)