 import math
monkeys = [[[89, 73, 66, 57, 64, 80], ["*", 3, 13, 6, 2]],[[83, 78, 81, 55, 81, 59, 69], ["+", 1, 3, 7, 4]], [[76, 91, 58, 85], ["*", 13, 7, 1, 4]], [[71, 72, 74, 76, 68], ["**", 2, 2, 6, 0]], [[98, 85, 84], ["+", 7, 19, 5, 7]], [[78], ["+", 8, 5, 3, 0]], [[86, 70, 60, 88, 88, 78, 74, 83], ["+", 4, 11, 1, 2]], [[81, 58], ["+", 5, 17, 3, 5]]]
inspects = [0,0,0,0,0,0,0,0]
temp = []
count = 0

def monkeyRound(monkeys):
    for x in range(len(monkeys)):
        for y in range(len(monkeys[x][0])):
            inspects[x] += 1
            if monkeys[x][1][0] == "+":
                monkeys[x][0][y] += monkeys[x][1][1]
            elif monkeys[x][1][0] == "*":
                monkeys[x][0][y] = monkeys[x][0][y]*monkeys[x][1][1]
            elif monkeys[x][1][0] == "**":
                monkeys[x][0][y] = monkeys[x][0][y]*monkeys[x][0][y]
            
            #comment for part 2
            monkeys[x][0][y] = math.floor(monkeys[x][0][y]/3)
        
            if monkeys[x][0][y]%monkeys[x][1][2] == 0:
                monkeys[monkeys[x][1][3]][0].append(monkeys[x][0][y])
            else:
                monkeys[monkeys[x][1][4]][0].append(monkeys[x][0][y])
        
            monkeys[x][0][y] = []
    return(monkeys)

for x in range(20):    
    monkeys = monkeyRound(monkeys)
    
    for x in range(len(monkeys)):
        for y in range(len(monkeys[x][0])):
            if monkeys[x][0][y] != []:
                temp.append(monkeys[x][0][y])
        monkeys[x][0] = temp
        temp = []
    #uncomment for part 2
    #for x in range(len(monkeys)):
    #    for y in range(len(monkeys[x][0])):
    #        monkeys[x][0][y] = monkeys[x][0][y]%(13*3*7*2*19*5*11*17)
print(inspects)
