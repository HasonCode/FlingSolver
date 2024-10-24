from matplotlib import pyplot as plt
import reverseFling as rf
from flingHelper import fling_solver,random_board_generator
import numpy as np
import time
# def points_against_time(fling_cap,board_size, logarithmic = True):
#     if logarithmic: plt.yscale("log")
#     data = gather_points(fling_cap,board_size)
#     plt.plot(data[0],data[1])
#     plt.savefig("time_vs_flings")

def gather_points(range_cap, board_size):
    data = []
    start = 2
    for i in range(start,range_cap+1):
        print(i)
        data.append([])
        for num in range(100):
            # print("num: "+str(num),i)
            random_flings = rf.random_builder_the_best(i,board_size)
            # print(random_flings)
            # print(random_flings)
            start_time = time.perf_counter_ns()
            solved = fling_solver(random_flings)
            # print(solved,random_flings)
            # if (solved[0]==None):
            #     print(random_flings)
            if solved[0]: 
                # print(data)
                data[i-start].append(time.perf_counter_ns()-start_time)
    return data,start

def points_against_time(fling_cap,board_size, logarithmic = True):
    if logarithmic: plt.yscale("log") 
    data,start = gather_points(fling_cap,board_size)
    plt.title("Time vs Number of Flings")
    plt.xlabel("Number of Flings")
    plt.ylabel("Time (ns)")
    avgys = [sum(data[i])/len(data[i]) for i in range(len(data))]
    avgxs = [i+start for i in range(len(data))]
    for i,item in enumerate(data):
        for element in item:
            # if i>1: print(element) 
            plt.plot(i+start,element,'bo',alpha = 0.2)
    plt.plot(avgxs, avgys, ".k:")
    plt.savefig("time_vs_flings")
    plt.show()


# print(fh.fling_solver([(7,5),(6,5),(3,5)]))
# print(gather_points(2,(10,10)))
points_against_time(10,(15,15))
# print(fling_solver([(1, 1), (1, 3)]))
