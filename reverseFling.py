from typing import Union
import flingHelper as fh
import random
def random_builder_the_best(num_flings, grid_size):
    for i in range(1000):
        if num_flings==0: return []
        grid_x,grid_y = grid_size[0],grid_size[1]
        possible_cords = []
        flings = []
        fling_states = []
        flag = [False]
        ret_val = 0
        for i in range(0,grid_x):
            for j in range(0,grid_y):
                if not((i==0 and j==grid_y-1 or j==0 and i == grid_x-1 or i==grid_x-1 and j == grid_y-1 or i==0 and j==0)):
                    possible_cords.append((i,j))
        if num_flings<=2: return one_two_generator(possible_cords,num_flings)
        cap = len(possible_cords)
        for i in range(cap):
            point = random.choice(possible_cords)
            possible_cords.remove(point)
            flings= [point]
            ret_val = board_builder_helper(flings,grid_x,grid_y,flag,fling_states,num_flings)
        for i in ret_val: 
            if len(i) == num_flings and fh.fling_solver(i)[0]:
                return i
    return []
    # if len(flings)<num_flings: return None
    # print(ret_val)

def fling_copy(flings):
    return [(i[0],i[1]) for i in flings ]

def board_builder_helper(flings,grid_x,grid_y,flag,fling_states,desired_flings):
    # print(grid_x,grid_y,flings)
    # print(flings)
    # print(desired_flings)
    # print(len(flings))
    if flag[0]==False and len(flings)==desired_flings:
        flag[0]=True
        fling_states.append(flings)
    if flag[0] or len(flings)==desired_flings:
        flag[0] = True
        return fling_states
    fling_states.append(fling_copy(flings))
    points = []
    if len(flings)!=desired_flings-1:
        points = gen_down_moves(flings[-1],grid_x,grid_y,flings,len(flings)==desired_flings-2)+gen_up_moves(flings[-1],grid_x,grid_y,flings,len(flings)==desired_flings-2)
        points+=gen_right_moves(flings[-1],grid_x,grid_y,flings,len(flings)==desired_flings-2)+gen_left_moves(flings[-1],grid_x,grid_y,flings,len(flings)==desired_flings-2)
    else: 
        points = gen_valid_final_point(flings[-1],grid_x,grid_y,flings)
        # print("Final Fling:",points)
    cap = len(points)
    for i in range(cap):
        flings_copy = fling_copy(flings)
        to_add = random.choice(points)
        points.remove(to_add)
        flings_copy.append(to_add)
        board_builder_helper(flings_copy,grid_x,grid_y,flag,fling_states,desired_flings)
    return fling_states

def in_corner(i,j,grid_x,grid_y):
    return (i==0 and j==grid_y-1 or j==0 and i == grid_x-1 or i==grid_x-1 and j == grid_y-1 or i==0 and j==0)

def gen_left_moves(prev_point,grid_x,grid_y,flings, is_second_to_last):
    moves = []
    range_start = 0 if is_second_to_last else 1
    for i in range(range_start,prev_point[1]-1):
        if 0<=prev_point[0]+1<grid_x and (prev_point[0]+1,i) not in flings:
            moves.append((prev_point[0]+1,i))
        if 0<=prev_point[0]-1<grid_x and (prev_point[0]-1,i) not in flings:
            moves.append((prev_point[0]-1,i))
    return moves
 
def gen_right_moves(prev_point,grid_x,grid_y,flings, is_second_to_last):
    moves = []
    range_end = grid_y if is_second_to_last else grid_y-1
    for i in range(prev_point[1]+2,range_end):
        # print("hi",flings)
        if 0<=prev_point[0]+1<grid_x and (prev_point[0]+1,i) not in flings:
            moves.append((prev_point[0]+1,i))
        if 0<=prev_point[0]-1<grid_x and (prev_point[0]-1,i) not in flings:
            moves.append((prev_point[0]-1,i))
    return moves

def gen_up_moves(prev_point,grid_x,grid_y,flings, is_second_to_last):
    moves = []
    range_start = 0 if is_second_to_last else 1
    for i in range(range_start,prev_point[0]-1):
        if 0<=prev_point[1]+1<grid_y and (i,prev_point[1]+1) not in flings:
            moves.append((i,prev_point[1]+1))
        if 0<=prev_point[1]-1<grid_y and (i,prev_point[1]-1) not in flings:
            moves.append((i,prev_point[1]-1))
    return moves

def gen_down_moves(prev_point,grid_x,grid_y,flings, is_second_to_last):
    moves = []
    range_end = grid_x if is_second_to_last else grid_x-1
    # print(prev_point,prev_point[0]+2,range_end)
    for i in range(prev_point[0]+2,range_end):
        # print("hi")
        if 0<=prev_point[1]+1<grid_y and (i,prev_point[1]+1) not in flings :
            moves.append((i,prev_point[1]+1))
        if 0<=prev_point[1]-1<grid_y and (i,prev_point[1]-1) not in flings:
            moves.append((i,prev_point[1]-1))
    return moves           

def gen_valid_final_point(prev_point,grid_x,grid_y,flings):
    points = []
    if len(flings)==1:
        for i in range(grid_x):
            for j in range(grid_y):
                if abs(prev_point[0]-i)>1 or abs(prev_point[1]-j)>1:
                    points.append((i,j))
        return points
    direction = find_intersection(flings[-2],prev_point,grid_x,grid_y)
    if "d" in direction:
        for point in range(prev_point[0]+2,grid_x):
            if grid_x>point>=0 and (point,prev_point[1]) not in flings and not surrounding_fling((point,prev_point[1]),flings):points.append((point,prev_point[1]))
    if "u" in direction:
        for point in range(prev_point[0]-1):
           if grid_x>point>=0 and (point,prev_point[1]) not in flings and not surrounding_fling((point,prev_point[1]),flings): points.append((point,prev_point[1]))
    if "r" in direction:
        for point in range(prev_point[1]+2,grid_y):
            if grid_y>point>=0 and (prev_point[0],point)not in flings and not surrounding_fling((prev_point[0],point),flings): points.append((prev_point[0],point))
    if "l" in direction:
        for point in range(prev_point[1]-1):
            if grid_y>point>=0 and (prev_point[0],point) not in flings and not surrounding_fling((prev_point[0],point),flings): points.append((prev_point[0],point))
    return points

def find_intersection(point1, point2,grid_x,grid_y):
    inter_points = [(point2[0]-1,point2[1],"d"),(point2[0]-1,point2[1],"u"),
                    (point2[0],point2[1]+1,"r"),(point2[0],point2[1]-1,"l")]
    ret_val = []
    for i in inter_points:
        if i[0] == point1[0] or i[1] == point1[1]:
            ret_val.append(i[2])
    return ret_val

def surrounding_fling(fling,flings):
    for i in range(fling[0]-1,fling[0]+2):
        for j in range(fling[1]-1, fling[1]+2):
            if (i,j)in flings: return True
    return False

def one_two_generator(possible_moves,num_flings):
    flings = []
    # print(possible_moves)
    while len(flings)<num_flings:
        # print(len(possible_moves))
        flings=[]
        choose = random.choice(possible_moves)
        possible_moves.remove(choose)
        flings.append(choose)
        next_move = []
        if num_flings==2:
            for i in possible_moves:
                if abs(i[0]-choose[0])>1 and i[1]==choose[1] or abs(i[1]-choose[1])>1 and i[0]==choose[0]:
                    next_move.append(i)
        if len(next_move)>=1:
            choose2 = random.choice(next_move)
            # possible_moves.remove(choose2)
            flings.append(choose2)
        # print(len(flings))
    # print(flings)
    return flings
grid = random_builder_the_best(2,(3,4))
print(grid)
# print("hello")
# flings = randomBuilder(4,(5,5))
# print(flings)
# grid = flingHelper.fling_solver(flings)
# flingHelper.print_grid(grid)
# solved = flingHelper.fling_solver(grid)
# print(solved[1])
# flingHelper.print_grid(flingHelper.to_grid(solved[0]))
# print(solved[1])