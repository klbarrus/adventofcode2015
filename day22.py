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
    'PMana' : 500,
    'PHit' : 50,
    'BHit' : 58,
    'BDam' : 9,
    'Shield' : 0,
    'Poison' : 0,
    'Recharge' : 0,
    'TotalMana' : 0,
}

playerWin = []

def done(gs):
    rv = False      # need to keep going
    if gs['PHit'] <= 0 or gs['BHit'] <= 0:
        rv = True   # player or boss is dead
    return rv

def playerarmor(gs):
    if gs['Shield'] > 0:
        return 7
    else:
        return 0

def printstats(gs):
    armor = playerarmor(gs)
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

def combat(sp, gs):
    print("-- Player turn --")
    printstats(gs)
    print("Player casts {}".format(sp))

# player turn
    applyEffects(gs)

# player casts a spell
    if sp == 'Drain':
        gs['PMana'] -= 73
        gs['PHit'] += 2
        gs['BHit'] -= 2
        gs['TotalMana'] += 73
    elif sp == 'Magic Missile':
        gs['PMana'] -= 53
        gs['BHit'] -= 4
        gs['TotalMana'] += 53
    elif sp == 'Poison':
        if gs['Poison'] == 0:
            gs['PMana'] -= 173
            gs['Poison'] = 6
            gs['TotalMana'] += 173
        else:
            return
    elif sp == 'Recharge':
        if gs['Recharge'] == 0:
            gs['PMana'] -= 229
            gs['Recharge'] = 5
            gs['TotalMana'] += 229
        else:
            return
    elif sp == 'Shield':
        if gs['Shield'] == 0:
            gs['PMana'] -= 113
            gs['Shield'] = 6
            gs['TotalMana'] += 113
        else:
            return

# check for win/loss
# ran out of mana; loss
    if gs['PMana'] < 0:
        return
# boss is dead; win
    if gs['BHit'] <= 0:
        playerWin.append(gs['TotalMana'])
        return

# boss turn
    print("-- Boss turn --")
    printstats(gs)

    applyEffects(gs)
    dam = max(gs['BDam'] - playerarmor(gs), 1)
    gs['PHit'] -= dam
    print("Boss attacks for {} damage".format(dam))
    
# check for win/loss
# player dead; loss
    if gs['PHit'] <= 0:
        return

# cast next round of spells
    gs_update = copy.deepcopy(gs)
    for sp in spells:
        combat(sp, gs_update)        

#minmana = 500
spells = sorted(SPELLS.keys())
#gs = copy.deepcopy(INIT_GAME_STATE)
for sp in spells:
    combat(sp, INIT_GAME_STATE)
#    if rv:
#        print("total mana spent: {}".format(gs['TotalMana']))
#    else:
#        print("boss win")

print("{}".format(playerWin))

#for sp in spells:
#    cast_spell(sp, 2)