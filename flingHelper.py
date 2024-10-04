sampleInput = [(1,4),(6,3),(2,1),(4,4)]
#[]
#[]
#[]
#[]
#[]
#[]
#[]


def findMoves(grid:list[list[int]],flings:list[tuple[int]]):
    potentialMoves = []
    for fling in flings:
        for right in range(fling[1]+1,len(grid[0])):
            if grid[fling[0]][right] == 1:
                potentialMoves.append([fling,(fling[0],right),"r"])
        for left in range(fling[1]-1,-1,-1):
            if grid[fling[0]][left] == 1:
                potentialMoves.append([fling,(fling[0],left),"l"])
        for up in range(fling[0]+1,len(grid)):
            if grid[up][fling[1]] == 1:
                potentialMoves.append([fling,(up,fling[1]),"d"])
        for down in range(fling[0]-1,-1,-1):
            if grid[down][fling[1]] == 1:
                potentialMoves.append([fling,(down,fling[1]),"u"])
    return potentialMoves



def flingStartup(flings:list[tuple])->list[list[int]]:
    if len(flings)<=0: return []
    maxDimensions,minDimensions = [0,0],[flings[0][0],flings[0][1]]
    for item in flings:
        if item[0]>maxDimensions[0]:
            maxDimensions[0]=item[0]+1
        if item[1]>maxDimensions[1]:
            maxDimensions[1]=item[1]+1
        if item[0]<minDimensions[0]:
            minDimensions[0]=item[0]
        if item[1]<minDimensions[1]:
            minDimensions[1]=item[1]
    grid = [[0 for row in range(minDimensions[1]-1,maxDimensions[1]+1)] for column in range(minDimensions[0]-1,maxDimensions[0]+1)]
    for i in range(len(flings)):
        flings[i]= (flings[i][0]-minDimensions[0]+1,flings[i][1]-minDimensions[1]+1)
    for fling in flings:
        grid[fling[0]][fling[1]]=1
    return grid

# def flingStartup(board:str):
#     for 
grid = flingStartup(sampleInput)

def flingBall(fling, toFling, grid, direction):
    if toFling==None:
        grid[fling[0]][fling[1]]=0
    elif direction=="d":
        grid[fling[0]][fling[1]]=0
        grid[toFling[0]-1][toFling[1]]=1
        nextFling = None
        for i in range(toFling[0]+1,len(grid)):
            if grid[i][fling[1]]==1:
                nextFling = (i,fling[0])
                i = len(grid)
        flingBall(toFling,nextFling,grid,direction)
    elif direction=="u":
        grid[fling[0]][fling[1]]=0
        grid[toFling[0]+1][toFling[1]]=1
        nextFling = None
        for i in range(toFling[0]-1,-1,-1):
            if grid[i][fling[1]]==1:
                nextFling = (i,fling[0])
                i = len(grid)
        flingBall(toFling,nextFling,grid,direction)
    elif direction=="l":
        grid[fling[0]][fling[1]]=0
        grid[toFling[0]][toFling[1]+1]=1
        nextFling = None
        for i in range(toFling[1]-1,-1,-1):
            if grid[fling[0]][i]==1:
                nextFling = (fling[0],i)
                i = len(grid)
        flingBall(toFling,nextFling,grid,direction)
    else:
        grid[fling[0]][fling[1]]=0
        grid[toFling[0]][toFling[1]-1]=1
        nextFling = None
        for i in range(toFling[1]+1,len(grid[0])):
            if grid[fling[0]][i]==1:
                nextFling = (fling[0],i)
                i = len(grid)
        flingBall(toFling,nextFling,grid,direction)

# flingBall(sampleInput[0],sampleInput[3],grid,"r")

def grabBoard(grid):
    flings = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                flings.append((i,j))
    return flings


def gridCopy(grid):
    return [[i for i in grid[j]] for j in range(len(grid))]

def flingRunner(grid:list[list[int]], flings:list[tuple], gridstates:list[tuple],intVal:str=""):
    gridstates.append((gridCopy(grid),intVal))
    potentialMoves = findMoves(grid,flings)
    for val,i in enumerate(potentialMoves):
        copyGrid = gridCopy(grid)
        flingBall(i[0],i[1],copyGrid,i[2])
        flingRunner(copyGrid,grabBoard(copyGrid),gridstates,intVal+str(val))
    for igrid in gridstates:
        if len(grabBoard(igrid[0]))==1:
            stringCode = igrid[1]
            rv = []
            for string in gridstates:
                if string[1] in stringCode:
                    rv.append(string[0])
            # rv.append(igrid[0])
            return rv
    return "No solution"

def printGrid(grid):
    for row in grid:
        print(row)
    print("\n\n")

# printGrid(grid)
output = flingRunner(grid,sampleInput,[])
for i in output:
    printGrid(i)