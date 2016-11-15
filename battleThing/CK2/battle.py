import random
import time
import combat_tactics


troopKillFactor = 0.015
lightInf = 0
heavyInf = 0

minCombatDays = 8


print('this is a CK2 battle simulation.')



def skirmish():
    lightInfantry = {'atk': 1 , 'def': 3}
    heavyInfantry = {'atk': 0.25 , 'def': 5}
    pikes = {'atk': 0.1 , 'def': 5 }
    lightCal = {'atk': 1 , 'def': 5 }
    knights = {'atk': 0.5 , 'def': 8 }
    archers = {'atk': 5 , 'def': 3 }
    horseArch = {'atk': 4 , 'def': 4 }
    elephant = {'atk' : 0.25, 'def': 6 }
    camels = {'atk' : 3, 'def': 2 }

def melee():
    lightInfantry = {'atk': 3 , 'def': 3 }
    heavyInfantry = {'atk': 6 , 'def': 4 }
    pikes = {'atk': 5 , 'def': 8 }
    lightCal = {'atk': 3 , 'def': 3 }
    knights = {'atk': 10 , 'def': 8 }
    archers = {'atk': 1 , 'def': 2 }
    horseArch = {'atk': 3 , 'def': 4 }
    elephant = {'atk' : 25, 'def': 10 }
    camels = {'atk' : 3 , 'def': 2 }

def pursuit():
    lightInfantry = {'atk': 3, 'def': 3}
    heavyInfantry = {'atk': 2, 'def': 2}
    pikes = {'atk': 0.2, 'def': 2 }
    lightCal = {'atk': 10, 'def': 8 }
    knights = {'atk': 8, 'def': 5 }
    archers = {'atk': 2, 'def': 3 }
    horseArch = {'atk': 7, 'def': 7 }

def combatTact():
    return


def battle():
    return