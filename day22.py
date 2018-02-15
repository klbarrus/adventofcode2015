#!/usr/bin/env python
# AdventOfCode 2015 Day 22

import copy

SPELLS = {
    'Magic Missile' : 53,
    'Drain' : 73,
    'Shield' : 113,
    'Poison' : 173,
    'Recharge' : 229,
}

INIT_GAME_STATE = {
    'Spells': [],
    'PMana' : 500,
    'PHit' : 50,
    'BHit' : 58,        # my puzzle input
    'BDam' : 9,         # my puzzle input
    'Shield' : 0,
    'Poison' : 0,
    'Recharge' : 0,
    'TotalMana' : 0,
}

def playerArmor(gs):
    if gs['Shield'] > 0:
        return 7
    else:
        return 0

def playerWin(gs):
    if gs['PHit'] > 0 and gs['PMana'] >= 0 and gs['BHit'] <= 0:
        return True
    return False

def printStats(gs):
    armor = playerArmor(gs)
    print("- Player has {} hit points, {} armor, {} mana".format(gs['PHit'], armor, gs['PMana']))
    print("- Boss has {} hit points".format(gs['BHit']))

def applyEffects(gs):
    if gs['Poison'] > 0:
        gs['Poison'] -= 1
        gs['BHit'] -= 3

    if gs['Recharge'] > 0:
        gs['Recharge'] -= 1
        gs['PMana'] += 101        
    
    if gs['Shield'] > 0:
        gs['Shield'] -= 1

def resolveCombatPlayer(sp, gs):
#    print("-- Player turn --")
#    printStats(gs)
#    print("Player casts {}".format(sp))
    applyEffects(gs)
# player casts a spell
    if sp == 'Drain':
        gs['PMana'] -= SPELLS['Drain']
        gs['PHit'] += 2
        gs['BHit'] -= 2
        gs['TotalMana'] += SPELLS['Drain']
    elif sp == 'Magic Missile':
        gs['PMana'] -= SPELLS['Magic Missile']
        gs['BHit'] -= 4
        gs['TotalMana'] += SPELLS['Magic Missile']
    elif sp == 'Poison':
        gs['PMana'] -= SPELLS['Poison']
        gs['Poison'] = 6
        gs['TotalMana'] += SPELLS['Poison']
    elif sp == 'Recharge':
        gs['PMana'] -= SPELLS['Recharge']
        gs['Recharge'] = 5
        gs['TotalMana'] += SPELLS['Recharge']
    elif sp == 'Shield':
        gs['PMana'] -= SPELLS['Shield']
        gs['Shield'] = 6
        gs['TotalMana'] += SPELLS['Shield']

def resolveCombatBoss(gs):
#    print("-- Boss turn --")
#    printStats(gs)
    applyEffects(gs)
# boss attacks    
    dam = max(gs['BDam'] - playerArmor(gs), 1)
    gs['PHit'] -= dam
#    print("Boss attacks for {} damage".format(dam))

# keep going until player or boss is dead, or player is out of mana
def endCondition(gs):
    if gs['PHit'] <= 0 or gs['PMana'] < 0 or gs['BHit'] <= 0:
        return True
    return False
    
def doCombat(sp, gs):
    gs['Spells'].append(sp)
    resolveCombatPlayer(sp, gs)
    if endCondition(gs):
        if playerWin(gs):
            WIN.append(gs)
        return
    resolveCombatBoss(gs)
    if endCondition(gs):
        if playerWin(gs):
            WIN.append(gs)
        return
    castable = ['Drain', 'Magic Missile']
    if gs['Poison'] == 0:
        castable.append('Poison')
    if gs['Recharge'] == 0:
        castable.append('Recharge')
    if gs['Shield'] == 0:
        castable.append('Shield')
    for i in castable:
        up = copy.deepcopy(gs)
        doCombat(i, up)

WIN = []
spells = sorted(SPELLS.keys())
gs = INIT_GAME_STATE
for sp in spells:
    up = copy.deepcopy(gs)
    doCombat(sp, up)

#print("winning game states:")
#for i in WIN:
#    print("---")    
#    print("{}".format(i))
#    print("")

num = len(WIN)
minmana = WIN[0]['TotalMana']
for i in WIN:
    if i['TotalMana'] < minmana:
        minmana = i['TotalMana']

print("{} ways for player to win".format(num))
print("min mana for player win: {}".format(minmana))
