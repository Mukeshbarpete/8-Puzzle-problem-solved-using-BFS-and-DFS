# import queue and stack from module
import copy
from queue import Queue
from queue import LifoQueue


# take initial state puzzle from user.
def getinitialstate():
    print("Enter 1 for Random grid.\nEnter 2 for user input .")
    choice = int(input("Enter your choice : "))
    lst = []
    if(choice==2):
        n = int(input("Enter order of Puzzle (blank = -1): "))
        for i in range(1, n+1):
            print("Enter row ", i, ": ", sep=" ", end=" ")
            lst.append(list(map(int, input().split())))
    else:
        lst = [[3, 2, 1],
                [4, 5, 6],
                [8, 7, -1]]

    return lst
# print initialstate of puzzle
def printinitial(initialstate):
    print("Initial state of puzzle :")
    n = len(initialstate)
    for i in range(n):
        for j in range(n):
            print(initialstate[i][j], end=" ")
        print()


def printtarget(target):
    n = len(target)
    print("Target state of puzzle :")
    for i in range(n):
        for j in range(n):
            print(target[i][j], end=" ")
        print()
# initialize target matrix puzzle
def gettarget(n):
    k = 1
    target = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(k)
            k+=1
        target.append(temp)
    target[n-1][n-1] = -1
    return target

# find black symbol position
def find_position_of_blank(statelist):
    for i in range(len(statelist)):
        for j in range(len(statelist[i])):
            if statelist[i][j] == -1:
                return (i, j)
    return (2, 2)

# compare initial and target state if equal return true else false
def compare_initial_target(initialstate, targetstate):
    for i in range(len(initialstate)):
        for j in range(len(initialstate[i])):
            if initialstate[i][j] != targetstate[i][j]:
                return False
    return True

#movement of tiles according to given direction
def leftstate(initialstate, x, y):
    initialstate[x][y],initialstate[x][y-1] = initialstate[x][y-1], initialstate[x][y]
    return initialstate

def rightstate(initialstate, x, y):
    initialstate[x][y], initialstate[x][y + 1] = initialstate[x][y + 1], initialstate[x][y]
    return initialstate

def upstate(initialstate, x, y):
    initialstate[x-1][y], initialstate[x][y] = initialstate[x][y], initialstate[x-1][y]
    return initialstate

def downstate(initialstate, x, y):
    initialstate[x][y], initialstate[x+1][y] = initialstate[x+1][y], initialstate[x][y]
    return initialstate

# dfsfunction for traversing puzzle using black moving left,right,top or bottom
def dfsfunction(initialstate, targetstate):
    dfscount = 0
    visited = {}
    stack = LifoQueue()
    stack.put(initialstate)
    lenoflist = len(initialstate)
    while (stack.empty() == False):
        initialstate = stack.get()
        # print(initialstate)
        if (compare_initial_target(initialstate, targetstate)):
            return dfscount
        k = tuple(map(tuple, initialstate))
        if k not in visited.keys():
            visited.update({k: 1})
            # print(visited)
            dfscount = dfscount + 1
            x, y = find_position_of_blank(initialstate)
            if (y < lenoflist - 1):
                rightlist = rightstate(copy.deepcopy(initialstate), x, y)
                stack.put(rightlist)
            if (y > 0):
                leftlist = leftstate(copy.deepcopy(initialstate), x, y)
                stack.put(leftlist)
            if (x > 0):
                uplist = upstate(copy.deepcopy(initialstate), x, y)
                stack.put(uplist)
            if (x < lenoflist - 1):
                downlist = downstate(copy.deepcopy(initialstate), x, y)
                stack.put(downlist)

    return -1 * dfscount
# bfsfunction for traversing puzzle using black moving left,right,top or bottom
def bfsfunction(initialstate, targetstate):
    bfscount = 0
    visited = {}
    queue = Queue()
    queue.put(initialstate)
    lenoflist = len(initialstate)
    while(queue.empty()==False):
        initialstate = queue.get()
        #print(initialstate)
        if(compare_initial_target(initialstate,targetstate)):
            return bfscount
        k = tuple(map(tuple,initialstate))
        if k not in visited.keys():
            visited.update({k: 1})
            #print(visited)
            bfscount = bfscount + 1
            x, y = find_position_of_blank(initialstate)
            if(y<lenoflist-1):
                rightlist = rightstate(copy.deepcopy(initialstate), x, y)
                queue.put(rightlist)
            if (y > 0):
                leftlist = leftstate(copy.deepcopy(initialstate), x, y)
                queue.put(leftlist)
            if(x>0):
                uplist = upstate(copy.deepcopy(initialstate), x, y)
                queue.put(uplist)
            if(x<lenoflist-1):
                downlist = downstate(copy.deepcopy(initialstate), x, y)
                queue.put(downlist)

    return -1*bfscount
if __name__ == '__main__':
    initialstate = getinitialstate()
    targetstate = gettarget(len(initialstate))
    # print(initialstate)
    printinitial(initialstate)
    # print(targetstate)
    printtarget(targetstate)
    # count number of step to reach the solution if they are reachable using dfs algorithm
    dfscount = dfsfunction(copy.deepcopy(initialstate), targetstate)
    # count number of step to reach the solution if they are reachable using bfs algorithm
    bfscount = bfsfunction(copy.deepcopy(initialstate), targetstate)
    # find difference
    difference = abs(dfscount-bfscount)

    #print output of both bfs and dfs with comparision
    if(dfscount<0 or bfscount<0):
        print("Problem Unsolvable !")
    else:
        print("Problem Solved !")
        print("Step taken in DFS algorithm : ", dfscount)
        print("step taken in BFS algorithm : ", bfscount)
        if bfscount > dfscount:
            print("DFS algorithm taken ", difference, " less steps : DFS perform better for given puzzle.")

        if dfscount > bfscount:
            print("BFS algorithm taken", difference, " step : BFS perform better for given puzzle.")
        if dfscount == bfscount:
            print("BFS and DFS algorithm taken same step: ", dfscount)