import pandas as pd
import math

dfInfo = pd.read_excel("stat.xlsx", 0)
dfAtk = pd.read_excel("stat.xlsx", 1)
dfScal = pd.read_excel("stat.xlsx", 2)
dfCalcCorrectId = pd.read_excel("stat.xlsx", 3)
dfAttackElementCorrect = pd.read_excel("stat.xlsx", 4)
dfCoef = pd.read_excel("stat.xlsx", 5)
dfStat = pd.read_excel("stat.xlsx", 6)
  
    
def getRequirement(weapon, statType):
    return dfInfo.loc[dfInfo["Name"] == weapon, "Required (" + statType +")"].to_numpy()[0]
       
def getFlatDamageValue(weapon, damageType, upgradeLevel):
    return dfAtk.loc[dfAtk["Name"] == weapon, damageType + str(upgradeLevel)].to_numpy()[0]
    
def getScalDamageValue(weapon, statType, upgradeLevel):
    return dfScal.loc[dfScal["Name"] == weapon, statType + str(upgradeLevel)].to_numpy()[0]
    
def getCalcCorrectId(weapon, damageType):
    return dfCalcCorrectId.loc[dfCalcCorrectId["Name"] == weapon, damageType].to_numpy()[0]
    
def getCoef(calcCorrectId, coefType):
    return dfCoef.loc[dfCoef["CalcCorrectId"] == calcCorrectId, coefType].to_numpy()[0]
    
def getStat(statType, level):
    return dfStat.loc[dfStat["Lvl"] == level, statType].to_numpy()[0]
    
def getAttackElementCorrectId(weapon):
    return dfCalcCorrectId.loc[dfCalcCorrectId["Name"] == weapon, "AttackElementCorrectId"].to_numpy()[0]
    
def isScaling(weapon, statType, damageType):
    return (dfAttackElementCorrect.loc[dfAttackElementCorrect["AttackElementCorrectParamId"] == getAttackElementCorrectId(weapon), statType + "/" + damageType].to_numpy()[0]) == 1
    
def isRequirementMet(weapon, statType, damageType, lvl):
    return not(isScaling(weapon, statType, damageType) and getRequirement(weapon, statType) > lvl)
    
def getCalcCorrectValue(weapon, statType, damageType, lvl):
    calcCorrectId = getCalcCorrectId(weapon, damageType)
    if isScaling(weapon, statType, damageType):
        if lvl > getCoef(calcCorrectId, "LevelCap1"):
            return getCoef(calcCorrectId, "Add1") + (getCoef(calcCorrectId, "Multiply1")*(lvl - getCoef(calcCorrectId, "LevelCap1"))/getCoef(calcCorrectId, "Divide1"))
        elif lvl > getCoef(calcCorrectId, "LevelCap2"):
            return getCoef(calcCorrectId, "Add2") + (getCoef(calcCorrectId, "Multiply2")*(lvl - getCoef(calcCorrectId, "LevelCap2"))/getCoef(calcCorrectId, "Divide2"))
        elif lvl > getCoef(calcCorrectId, "LevelCap3"):
            return getCoef(calcCorrectId, "Add3") + (getCoef(calcCorrectId, "Multiply3")*(1 + getCoef(calcCorrectId, "Coef1") + getCoef(calcCorrectId, "Coef2")*(1 + getCoef(calcCorrectId, "Coef1") + getCoef(calcCorrectId, "Coef2")*(lvl-getCoef(calcCorrectId, "LevelCap3"))/getCoef(calcCorrectId, "Divide3"))**getCoef(calcCorrectId, "Coef3")))
        else:
            return getCoef(calcCorrectId, "Multiply4")*((lvl - 1)/getCoef(calcCorrectId, "Divide4"))**getCoef(calcCorrectId, "Coef3")
    else :
        return 0
    
def scalingElementDamage(weapon, statType, damageType, upgradeLevel, lvl):
    return getFlatDamageValue(weapon, damageType, upgradeLevel) * getScalDamageValue(weapon, statType, upgradeLevel) * getCalcCorrectValue(weapon, statType, damageType, lvl) / 100

    
def getScalingDamage(weapon, damageType, upgradeLevel, statsLvl):
    listStats = ["Str", "Dex", "Int", "Fai", "Arc"]
    switcher={"Str":0, "Dex":1, "Int":2, "Fai":3, "Arc":4}
    damage = 0
    for stat in listStats:
        if isRequirementMet(weapon, stat, damageType, statsLvl[switcher.get(stat)]):
            damage += scalingElementDamage(weapon, stat, damageType, upgradeLevel, statsLvl[switcher.get(stat)])
        else:
            return -0.4 * getFlatDamageValue(weapon, damageType, upgradeLevel)
        
    return damage
    
def getStatDefense(runeLevel, level):
    if runeLevel <= 71:
        defense = 40 + 60 * ((runeLevel + 79 - 1) / 149)
    elif runeLevel <= 91:
        defense = 100 + 20 * ((runeLevel + 79 - 150) / 20)
    elif runeLevel <= 161:
        defense = 120 + 15 * ((runeLevel + 79 - 170) / 70)
    else:
        defense = 135 + 20 * ((runeLevel + 79 - 240) / 552)
    if level <= 30:
        defense += 10*(level / 30)
    elif runeLevel <= 40:
        defense += 10 + 5 * ((level - 30) / 10)
    elif runeLevel <= 60:
        defense += 15 + 15 * ((level - 40) / 20)
    else:
        defense += 30 + 10 * ((level - 60) / 39)
    return math.floor(defense)
    
def getStatResistance(runeLevel, level):
    if (runeLevel <= 71 ):
        defense = 75 + 30 * ((runeLevel + 79 - 1) / 149)
    elif(runeLevel <= 111 ):
        defense = 105 + 40 * ((runeLevel + 79 - 150) / 40)
    elif(runeLevel <= 161 ):
        defense = 145 + 15 * ((runeLevel + 79 - 190) / 50)
    else:
        defense = 160 + 20 * ((runeLevel + 79 - 240) / 552)
    if level <= 30 :
        defense += 0
    elif(runeLevel <= 40 ):
        defense += 30 * ((level - 30) / 10)
    elif runeLevel <= 60 :
        defense += 30 + 10 * ((level - 40) / 20)
    else:
        defense += 40 + 10 * ((level - 60) / 39)
    return math.floor(defense)
    
class Build:    
    def __init__(self, weapon, upgradeLevel, vigor, mind, endurance, strength, dexterity, intelligence, faith, arcane):
        self.physFlatDamage = math.floor(getFlatDamageValue(weapon, "Phys", upgradeLevel))
        self.magFlatDamage = math.floor(getFlatDamageValue(weapon, "Mag", upgradeLevel))
        self.fireFlatDamage = math.floor(getFlatDamageValue(weapon, "Fire", upgradeLevel))
        self.lighFlatDamage = math.floor(getFlatDamageValue(weapon, "Ligh", upgradeLevel))
        self.holyFlatDamage = math.floor(getFlatDamageValue(weapon, "Holy", upgradeLevel))
        self.physScalDamage = math.floor(getScalingDamage(weapon, "Phys", upgradeLevel, [strength, dexterity, intelligence, faith, arcane]))
        self.magScalDamage = math.floor(getScalingDamage(weapon, "Mag", upgradeLevel, [strength, dexterity, intelligence, faith, arcane]))
        self.fireScalDamage = math.floor(getScalingDamage(weapon, "Fire", upgradeLevel, [strength, dexterity, intelligence, faith, arcane]))
        self.lighScalDamage = math.floor(getScalingDamage(weapon, "Ligh", upgradeLevel, [strength, dexterity, intelligence, faith, arcane]))
        self.holyScalDamage = math.floor(getScalingDamage(weapon, "Holy", upgradeLevel, [strength, dexterity, intelligence, faith, arcane]))
        self.runeLevel = -79 + vigor + mind + endurance + strength + dexterity + intelligence + faith + arcane
        self.HP = getStat("HP", vigor)
        self.FP = getStat("FP", mind)
        self.stamina = getStat("Stamina", endurance)
        self.equipLoad = getStat("EquipLoad", endurance)
        self.physicalDefense = getStatDefense(self.runeLevel, strength)
        self.magicDefense = getStatDefense(self.runeLevel, intelligence)
        self.fireDefense = getStatDefense(self.runeLevel, vigor)
        self.lightningDefense = getStatDefense(self.runeLevel, 0)
        self.holyDefense = getStatDefense(self.runeLevel, arcane)
        self.immunity = getStatResistance(self.runeLevel, vigor)
        self.robustness = getStatResistance(self.runeLevel, endurance)
        self.focus = getStatResistance(self.runeLevel, mind)
        self.vitality = getStatResistance(self.runeLevel, arcane)