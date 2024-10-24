sampleInput = [(0,0),(2,0),(3,0),(4,0),(2,4),(1,6),(5,5),(6,5)]
import time
import random
import multiprocessing as mp
#Attempt 2.0
def find_moves(flings):
    move_list = []
    for i in flings:
        if can_fling_up(i,flings):
            move_list.append((i,can_fling_up(i,flings),"n"))
        if can_fling_down(i,flings):
            move_list.append((i,can_fling_down(i,flings),"s"))
        if can_fling_left(i,flings): 
            move_list.append((i,can_fling_left(i,flings),"w"))
        if can_fling_right(i,flings): 
            move_list.append((i,can_fling_right(i,flings),"e"))
    return move_list


def can_fling_up(fling,flings):
    ret_fling = False
    for i in flings:
        if i != fling and i[0]<fling[0]-1 and i[1]==fling[1] and (ret_fling==False or i[0]>ret_fling[0]):
            ret_fling=i
    return ret_fling

def can_fling_down(fling,flings):
    ret_fling = False
    for i in flings:
        if i != fling and i[0]>fling[0]+1 and i[1]==fling[1] and (ret_fling==False or i[0]<ret_fling[0]):
            ret_fling = i
    return ret_fling

def can_fling_left(fling,flings):
    ret_fling = False
    for i in flings:
        if i != fling and i[1]<fling[1]-1 and i[0]==fling[0] and (ret_fling==False or i[1]>ret_fling[1]):
            ret_fling = i 
    return ret_fling

def can_fling_right(fling,flings):
    ret_fling = False
    for i in flings:
        if i != fling and i[1]>fling[1]+1 and i[0]==fling[0] and(ret_fling==False or i[1]>ret_fling[1]):
            return i
    return ret_fling

def fling_up(fling, flings, to_fling):
    flings.remove(fling)
    if (to_fling):
        flings.append((to_fling[0]+1,to_fling[1]))
        fling_up(to_fling,flings,can_fling_up(to_fling,flings))
                
def fling_down(fling, flings,to_fling):
    flings.remove(fling)
    if (to_fling):
        flings.append((to_fling[0]-1,to_fling[1]))
        fling_down(to_fling,flings,can_fling_down(to_fling,flings))

def fling_right(fling, flings,to_fling):
    flings.remove(fling)
    if (to_fling):
        flings.append((to_fling[0],to_fling[1]-1))
        fling_right(to_fling,flings,can_fling_right(to_fling,flings))

def fling_left(fling, flings,to_fling):
    flings.remove(fling)
    if (to_fling):
        flings.append((to_fling[0],to_fling[1]+1))
        fling_left(to_fling,flings,can_fling_left(to_fling,flings))
    

def fling_handler(move,flings):
    # print(move)
    if move[2]=="n": fling_up(move[0],flings,move[1])
    elif move[2]=="s": fling_right(move[0],flings,move[1])
    elif move[2]=="w": fling_left(move[0],flings,move[1])
    else: fling_right(move[0],flings,move[1])
    
def fling_copy(flings):
    return [(i[0],i[1]) for i in flings]

def fling_runner(flings:list,fling_states:list=[],path_taken:str="",iteration:list[int]=[0], printing:bool=False, mainCount = 0,timeSinceEpoch=0, flag = [False]):
    fling_states.append((flings.copy(),path_taken,time.perf_counter_ns()))
    # print(flings,flag)
    if len(flings) == 1 or flag[0]==True:
        flag[0]=True
        return fling_states
    moves = find_moves(flings)
    # print(moves)
    for move in moves:
        mainCount+=1
        timeSinceEpoch = time.perf_counter_ns()
        # print(flings,flag)
        temp_flings = fling_copy(flings)
        iteration[0]+=1
        fling_handler(move,temp_flings)
        fling_runner(temp_flings,fling_states,path_taken+f"{move[0]}, {move[2]} to {move[1]}\n",iteration,timeSinceEpoch=timeSinceEpoch, flag = flag)
    return fling_states

def to_grid(flings):
    if len(flings)==0: return ""
    min_row,min_col,max_row,max_col = flings[0][0],flings[0][1],flings[0][1],flings[0][1]
    for fling in flings:
        if fling[0]<min_row: min_row=fling[0]
        if fling[0]>max_row: max_row = fling[0]
        if fling[1]<min_col: min_col = fling[1]
        if fling[1]>max_col: max_col = fling[1]
    row_adder = -min_row
    col_adder = -min_col
    max_col += col_adder
    max_row += row_adder
    grid = [["-"  for i in range(max_col+3)] for j in range(max_row+3)]
    for i,item in enumerate(flings):
        grid[item[0]+row_adder+1][item[1]+col_adder+1] = str(i) 
    return grid

def fling_solver(flings,**kwargs):
    start_time = time.perf_counter_ns()
    iterations = [0]
    flag = [False]
    ret_val = fling_runner(flings,[],iteration=iterations,flag=flag,**kwargs)
    # print(len(ret_val))
    for i,fling_state in enumerate(ret_val):
        # print(fling_state)
        if len(fling_state[0])==1:
            # print(fling_state[2],start_time)
            return (fling_state[0][0],fling_state[1],time.perf_counter_ns()-start_time,i)
    return (None,"No Solution",len(ret_val)-1,0)
    
def print_grid(grid):
    for row in grid:
        print(row)
    print("\n")

def squarer(x):
    return x**2
def parallel_test(nums):
    mp.Pool()
# og_grid = [(3, 4), (2, 1), (3, 3), (1, 3)]
# flings2 = [(0,0),(2,0)]
# print_grid(to_grid(sampleInput))
# startTime = time.time_ns()
# vals = fling_solver(og_grid)
# print(vals)
# endTime = time.time_ns()
# print(endTime-startTime)
# val_g = vals
# print_grid(to_grid([vals[0]]))
# printrid(grid)
# output = flingRunner(grid,sampleInput,[])
# print(fling_solver(og_grid))
# print(f"{output[1]}\n")
# printGrid(output[0])
# print_grid(to_grid([(7,5),(6,5),(3,5),(1,5),(8,5),(9,3),(6,4),(2,4)]))
# print(fling_solver([(7,5),(6,5),(3,5),(1,5),(8,5),(9,3),(6,4),(2,4)]))

def random_board_generator(num_flings,grid_size):
    while True:
    #    print("hi")
       flings = []
       possible_moves = [(i,j)for i in range(grid_size[0])for j in range(grid_size[1])]
       for j in range (num_flings):
           choose = random.choice(possible_moves)
           possible_moves.remove(choose)
           flings.append(possible_moves)
    #    print(len(flings))
       if (fling_solver(flings)[0]!=None):
        return flings
    return None