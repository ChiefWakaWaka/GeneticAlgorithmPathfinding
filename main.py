# TODO: Fix scoring to award actual progress
# TODO: Add import from spreadsheet map

import numpy as np
import random
import math

# NOTE: Creates arrays to hold information about map and pathfinders as well as variables for parameters
map = np.array([[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 0, 0, 3, 1],
                [1, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 0, 0, 0, 1],
                [1, 2, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1]])

botCount = 10
instructions = np.size(map)
rounds = 1000
mutationChance = 25
startX, startY = np.where(map == 3)
goalX, goalY = np.where(map == 2)

bot = np.zeros(shape=(botCount, instructions))
botScore = np.zeros(shape=(botCount,1))

# NOTE: Setup random starting instructions
for r in range(botCount):
    for c in range(instructions):
        bot[r][c] = random.randint(1,4)

for i in range(rounds):
# NOTE: run instructions and find scores
    for r in range(botCount):
        cRow, cCol = int(startX), int(startY)
        points = 0
        #score = 0
        for c in range(instructions):
            if(map.item(cRow, cCol) == 0 or map.item(cRow, cCol) == 3):
                if(bot.item(r,c) == 1):
                    cRow += 1
                elif(bot.item(r,c) == 2):
                    cRow -= 1
                elif(bot.item(r,c) == 3):
                    cCol -= 1
                else:
                    cCol += 1
            elif(map.item(cRow, cCol) == 1):
                score = 1/math.sqrt((float(goalX) - cRow)**2 + (float(goalY) - cCol)**2)
                break
            elif(map.item(cRow, cCol) == 2):
                score = 50 / points
                break
            points += 1
        botScore[r][0] = score
    maxIndex = np.argmax(botScore)

# NOTE: Update instructions and mutate
    for c in range(instructions):
        bot[0][c] = bot.item(maxIndex, c)
    for r in range(botCount - 1):
        for c in range(instructions):
            bot[r+1][c] = bot.item(maxIndex, c)
            if(random.randint(1, mutationChance) == 1):
                bot[r+1][c] = random.randint(1,4)
# NOTE: Change instructions to readable information
sol = []
for c in range(points):
    if(bot.item(0, c) == 1):
        sol.append("Down")
    elif(bot.item(0, c) == 2):
        sol.append("Up")
    elif(bot.item(0, c) == 3):
        sol.append("Left")
    elif(bot.item(0, c) == 4):
        sol.append("Right")

print(sol)
