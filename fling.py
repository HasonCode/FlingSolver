sampleInput = [(0,0),(3,4),(5,6)]
def flingStartup(flings:list[tuple]):
    maxDimensions = [0,0]
    for i in flings:
        if i[0]+1>maxDimensions[0]:
            maxDimensions[0]=i[0]+1
        if i[1]+1>maxDimensions[1]:
            maxDimensions[1]=i[1]+1
    grid = [[0 for row in maxDimensions[0]] for column in maxDimensions[1]]
    for fling in flings:
        grid[fling[0]][fling[1]]=1
    return grid

def findMoves(grid,flings):
    potentialMoves = []
    for fling in flings:
        rightSum = sum(grid[fling[0]][fling[1]:])-1
        belowSum = sum([grid[i][fling[0]] for i in range(fling[0]+1)])-1
        aboveSum = sum([grid[i][fling[0]] for i in range(fling[0],len(grid))])-1
        leftSum = sum(grid[fling[0]][0:fling[1]+1])-1
        if rightSum>0 and grid[fling[0]][fling[1]+1]!=1: potentialMoves+=(fling,"r")
        if leftSum>0 and grid[fling[0]][fling[1]-1]!=1: potentialMoves+=(fling,"l")
        if belowSum>0 and grid[fling[0]-1][fling[1]]!=1: potentialMoves+=(fling,"d")
        if aboveSum>0 and grid[fling[0]+1][fling[1]]!=1: potentialMoves+=(fling,"u")
    return potentialMoves

def remover(posSet, pos):
    for i in posSet:
        if i == pos:
            posSet.remove(i)
    return posSet

def processMove(grid,move,flings):
    grid2 = [[i for i in grid[j]] for j in range(len(grid[0]))]
    move1 = move[0][0]
    move2 = move[0][1]
    if move[1]=="r":
        for j in range(len(grid[0])):
            if grid[move[0][0]][j] == 1:
                grid[move[0][0]][j-1] = 1
                grid[move1][j] = 0
                grid[move1][move2] = 0
                remover(flings,(move1,j))
                remover(flings,(move1,move2))
                flings.append((move1,j-1))
    if move[1]=="l":
        for j in range(len(grid[0])):
            if grid[move[0][0]][j] == 1:
                grid[move[0][0]][j+1] = 1
                grid[move1][j] = 0
                grid[move1][move2] = 0
                remover(flings,(move1,j))
                remover(flings,(move1,move2))
                flings.append((move1,j+1))
                
    if move[1]=="u":
        for j in range(len(grid)):
            if grid[j][move2] == 1:
                grid[j-1][move2] = 1
                grid[j][move2] = 0
                grid[move1][move2] = 0
                remover(flings,(j,move2))
                remover(flings,(move1,move2))
                flings.append((j-1,move2))
                
    if move[1]=="d":
        for j in range(len(grid)):
            if grid[j][move2] == 1:
                grid[j+1][move2] = 1
                grid[j][move2] = 0
                grid[move1][move2] = 0
                remover(flings,(j,move2))
                remover(flings,(move1,move2)) 
                flings.append((j+1,move2))
                
    return grid
def flingRunner(grid,flings):
     moves = findMoves(grid,flings)
     