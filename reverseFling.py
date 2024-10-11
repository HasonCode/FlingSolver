from typing import Union
# import flingHelper
import random
def randomBuilder(numFlings, gridSize):
    # grid = [[0 for i in range(gridSize[0])] for j in range(gridSize[1])]
    # grid[random.randint(0,gridSize[0]-1)][random.randint(0,gridSize)]
    flings = []
    flings.append((random.randint(0,gridSize[0]),random.randint(0,gridSize[1])))
    for i in range(numFlings-1):
        print("hi")
        genValidMove(gridSize,flings)
def genValidMove(gridSize, flings):
    listy =  [leftMove(gridSize,flings),rightMove(gridSize,flings),upMove(gridSize, flings), downMove(gridSize,flings)]
    while False in listy:
        listy.remove(False)
    bally = random.choice(listy)
    flings.append(bally)
    
def downMove(gridSize, flings):
    if gridSize[0]<=flings[-1][0]: return False
    row = flings[-1][0]-random.randint(1,gridSize[0]-flings[-1][0]-1)
    col = flings[-1][1]
    return (row,col) 
def upMove(gridSize, flings):
    if flings[-1][0]<gridSize[0]:
        return (flings[-1][0]+random.randint(1,gridSize[0]-flings[-1][0]-1),-flings[-1][0]-1),flings[-1][1]
    else: False 
def leftMove(gridSize, flings):
    if flings[-1][1]>=1:
        return (flings[-1][0],flings[-1][1]-random.randint(1,gridSize[1]-flings[-1][1]-1)) 
    else: False
def rightMove(gridSize, flings):
    if flings[-1][1]<gridSize[0]:
        return (flings[-1][0],flings[-1][1]+random.randint(1,gridSize[1]-flings[-1][1]-1)) 
    else: False

# print("hello")
# flings = randomBuilder(4,(5,5))
# grid = flingHelper.flingStartup(flings)
# flingHelper.printGrid(grid)