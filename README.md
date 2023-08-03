# 8-Puzzle-problem-solved-using-BFS-and-DFS
The task is to check if we can reach from any random start grid to the mentioned target grid by moving the Blank space ('B'). In one step, the Blank space can move either top or down or left or right.

1. Compare Breadth First Search(BFS) and Depth First Search(DFS) with respect to
the number of steps required to reach the solution if they are reachable.

2. Comment on which algorithm will be faster and when, by mentioning proper
intuition and examples.

1.	Algorithm:

STEP 1: Ask user to enter input manually or randomize.

STEP 2: Take the initial state of the puzzle from user.

STEP 2: Check whether the puzzle is solvable or not.

STEP 3: If puzzle is NOT solvable, output printing “Puzzle is not solvable”  

STEP 4: If puzzle is Solvable, calculate no. of steps taken by BFS and DFS algorithm           to solve the puzzle. We are taking RIGHT, LEFT,  UP and DOWN move in puzzle. 

STEP 5: Compare the steps taken and output which approach (BFS/DFS) performs better for the given input puzzle.
