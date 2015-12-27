#Magic Missile costs 53 mana. It instantly does 4 damage.
#Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
#Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
#Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
#Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

spells = [
 # name,     cost,  mana, damage, heals, armor, duration
 ['Shield',   113,     0,      0,     0,     7, 6],
 ['Poison',   173,     0,      3,     0,     0, 6],
 ['Recharge', 229,   101,      0,     0,     0, 5],
 ['Drain',     73,     0,      2,     2,     0, None],
 ['Missile',   53,     0,      4,     0,     0, None]
]

COST = 1
MANA = 2
DAMAGE = 3
HEALS = 4
ARMOR = 5
DURATION = 6

myMana = 500
myHP = 50

bossHP = 71
bossDamage = 10

def applyEffects(effects, myHP, myMana, bossHP, step):
    effects2 = []
    myArmor = 0
    for effect in effects:
        myMana += effect[MANA]
        bossHP -= effect[DAMAGE]
        myHP += effect[HEALS]
        myArmor = max(myArmor, effect[ARMOR])
        effect[DURATION] -= 1
        if effect[DURATION] > 0:
            effects2.append(effect)
        #print " " * step, "apply", myMana, myHP, myArmor, bossHP, effect
    return (effects2, myArmor, myHP, myMana, bossHP)

def fight(myHP, myMana, bossHP, bossDamage, effects, manaSpent, spellsSoFar, step):
    bestResult = 100000000
    bestSpells = None

    # My attack; first apply effects, then choose best line of attack
    myHP -= 1
    effects, myArmor, myHP, myMana, bossHP = applyEffects(effects, myHP, myMana, bossHP, step)
    for spell in spells:
        myArmor2, myHP2, myMana2, bossHP2, manaSpent2 = myArmor, myHP, myMana, bossHP, manaSpent
        effects2 = [e[:] for e in effects]
        spellsSoFar2 = spellsSoFar + [spell[0]]
        if myMana2 >= spell[COST] and len(filter(lambda x: x[0] == spell[0], effects2)) == 0:
            #print " " * step, spell[0][0:6], myHP2, bossHP2, myMana2, [e[0] for e in effects2]
            myMana2 -= spell[COST]
            manaSpent2 += spell[COST]
            if spell[DURATION] != None:
                #print " " * step, "effect", spell, effects2
                effects2.append(spell[:])
            else:
                myMana2 += spell[MANA]
                bossHP2 -= spell[DAMAGE]
                myHP2 += spell[HEALS]
            if bossHP <= 0:
                if manaSpent2 < bestResult:
                   bestResult = manaSpent2
                   bestSpells = spellsSoFar2
                   #print " " * step, "=> ++", bestResult, bestSpells
            else:
                # Boss attacks
                effects2, myArmor2, myHP2, myMana2, bossHP2 = applyEffects(effects2, myHP2, myMana2, bossHP2, step)
                if bossHP2 <= 0:
                    if manaSpent2 < bestResult:
                       bestResult = manaSpent2 
                       bestSpells = spellsSoFar2
                       #print " " * step, "=> ++", bestResult, bestSpells
                else:
                    myHP2 -= bossDamage - myArmor2
                    if myHP2 <= 0:
                        # Lose
                        #print " " * step, "=> --"
                        pass
                    else:
                        (nextBestResult, nextBestSpells) = fight(myHP2, myMana2, bossHP2, bossDamage, effects2, manaSpent2, spellsSoFar2, step+1)
                        if nextBestResult < bestResult:
                            bestResult = nextBestResult
                            bestSpells = nextBestSpells
        else:
            if myMana < spell[COST]:
                #print " " * step, "could not use", spell[0], myMana
                pass
            else:
                #print " " * step, "could not use", spell[0], effects
                pass
    return (bestResult, bestSpells)

print fight(myHP, myMana, bossHP, bossDamage, [], 0, [], 0)

