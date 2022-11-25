import math

def statHP(level):
    listHP = [300,304,312,322,334,347,362,378,396,414,434,455,476,499,522,547,572,598,624,652,680,709,738,769,800,833,870,910,951,994,1037,1081,1125,1170,1216,1262,1308,1355,1402,1450,1476,1503,1529,1555,1581,1606,1631,1656,1680,1704,1727,1750,1772,1793,1814,1834,1853,1871,1887,1900,1906,1912,1918,1924,1930,1936,1942,1948,1954,1959,1965,1971,1977,1982,1988,1993,1999,2004,2010,2015,2020,2026,2031,2036,2041,2046,2051,2056,2060,2065,2070,2074,2078,2082,2086,2090,2094,2097,2100]
    return listHP[level-1]

def statFP(level):
    listFP = [40,43,46,49,52,55,58,62,75,78,82,85,88,91,95,100,105,110,116,121,126,131,137,142,147,152,158,163,168,173,179,184,189,194,200,207,214,221,228,235,242,248,255,262,268,275,281,287,293,300,305,311,317,322,328,333,338,342,346,350,352,355,357,360,362,365,367,370,373,375,378,380,383,385,388,391,393,396,398,401,403,406,408,411,414,416,419,421,424,426,429,432,434,437,439,442,444,447,450]
    return listFP[level-1]
  
def statStamina(level):
    listStamina = [80,81,83,85,87,88,90,92,94,96,97,99,101,103,105,106,108,110,111,113,115,116,118,120,121,123,125,126,128,130,131,132,133,135,136,137,138,140,141,142,143,145,146,147,148,150,151,152,153,155,155,155,155,156,156,156,157,157,157,158,158,158,158,159,159,159,160,160,160,161,161,161,162,162,162,162,163,163,163,164,164,164,165,165,165,166,166,166,166,167,167,167,168,168,168,169,169,169,170]
    return listStamina[level-1]

def statEquipLoad(level):
    listEquipLoad = [45.0,45.0,45.0,45.0,45.0,45.0,45.0,45.0,46.6,48.2,49.8,51.4,52.9,54.5,56.1,57.7,59.3,60.9,62.5,64.1,65.6,67.2,68.8,70.4,72.0,73.0,74.1,75.2,76.4,77.6,78.9,80.2,81.5,82.8,84.1,85.4,86.8,88.1,89.5,90.9,92.3,93.7,95.1,96.5,97.9,99.4,100.8,102.2,103.7,105.2,106.6,108.1,109.6,111.0,112.5,114.0,115.5,117.0,118.5,120.0,121.0,122.1,123.1,124.1,125.1,126.2,127.2,128.2,129.2,130.3,131.3,132.3,133.3,134.4,135.4,136.4,137.4,138.5,139.5,140.5,141.5,142.6,143.6,144.6,145.6,146.7,147.7,148.7,149.7,150.8,151.8,152.8,153.8,154.9,155.9,156.9,157.9,159.0,160.0]
    return listEquipLoad[level-1]

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

def stats(vigor, mind, endurance, strength, dexterity, intelligence, faith, arcane):
    stats = {}
    runeLevel = -79 + vigor + mind + endurance + strength + dexterity + intelligence + faith + arcane
    stats = {"runeLevel":runeLevel,
        "HP":statHP(vigor),
        "FP":statFP(mind),
        "stamina":statStamina(endurance),
        "equipLoad":statEquipLoad(endurance),
        "physicalDefense":getStatDefense(runeLevel, strength),
        "magicDefense":getStatDefense(runeLevel, intelligence),
        "fireDefense":getStatDefense(runeLevel, vigor),
        "lightningDefense":getStatDefense(runeLevel, 0),
        "holyDefense":getStatDefense(runeLevel, arcane),
        "immunity":getStatResistance(runeLevel, vigor),
        "robustness":getStatResistance(runeLevel, endurance),
        "focus":getStatResistance(runeLevel, mind),
        "vitality":getStatResistance(runeLevel, arcane)}
    return stats