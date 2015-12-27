#Weapons:    Cost  Damage  Armor
#Dagger        8     4       0
#Shortsword   10     5       0
#Warhammer    25     6       0
#Longsword    40     7       0
#Greataxe     74     8       0
#
#Armor:      Cost  Damage  Armor
#Leather      13     0       1
#Chainmail    31     0       2
#Splintmail   53     0       3
#Bandedmail   75     0       4
#Platemail   102     0       5
#
#Rings:      Cost  Damage  Armor
#Damage +1    25     1       0
#Damage +2    50     2       0
#Damage +3   100     3       0
#Defense +1   20     0       1
#Defense +2   40     0       2
#Defense +3   80     0       3
#
#Hit Points: 100
#Damage: 8
#Armor: 2
#

import itertools

weapons = [
  ['Dagger', 8, 4, 0],
  ['Shortsword', 10, 5, 0],
  ['Warhammer', 25, 6, 0],
  ['Longsword', 40, 7, 0],
  ['Greataxe', 74, 8, 0]
]

armor = [
  ['None', 0, 0, 0],
  ['Leather', 13, 0, 1],
  ['Chainmail', 31, 0, 2],
  ['Splintmail', 53, 0, 3],
  ['Bandedmail', 75, 0, 4],
  ['Platemail', 102, 0, 5]
]

rings = [
  ['Damage +1', 25, 1, 0],
  ['Damage +2', 50, 2, 0],
  ['Damage +3', 100, 3, 0],
  ['Defense +1', 20, 0, 1],
  ['Defense +2', 40, 0, 2],
  ['Defense +3', 80, 0, 3]
]

boss = [100, 8, 2]

weaponOptions = [[w] for w in weapons]
armorOptions = [[a] for a in armor]
ringOptions = [[]] + [[r] for r in rings] + list(itertools.combinations(rings, 2))

print weaponOptions
print armorOptions
print ringOptions

def fight(boss, me):
    # boss and me are: [hitpoints, damage, armor]
    while True:
        # me attacks
        damage = max(1, me[1] - boss[2])
        boss[0] -= damage
        if boss[0] <= 0:
            return True
        # boss attacks
        damage = max(1, boss[1] - me[2])
        me[0] -= damage
        if me[0] <= 0:
            return False

def evaluate(items):
    cost = sum(map(lambda item: item[1], items))
    damage = sum(map(lambda item: item[2], items))
    armor = sum(map(lambda item: item[3], items))
    return (cost, fight(boss[:], [100, damage, armor]))

maxCost = 0
for w in weaponOptions:
    for a in armorOptions:
        for r in ringOptions:
            (cost, iWin) = evaluate(w+a+list(r))
            if not iWin:
                maxCost = max(maxCost, cost)
print maxCost

