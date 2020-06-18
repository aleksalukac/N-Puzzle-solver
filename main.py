from copy import deepcopy
import time
import sys


class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 

    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if getHeuristicDistance(self.queue[i]) < getHeuristicDistance(self.queue[max]): 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit() 

def solved():
    board = []
    row = []
    for i in range(1, boardSize + 2):
        if(i % dim == 1 and i > 1):
            board.append(row)
            row = []
        row.append(i % boardSize)

    return board

def getZeroPosition(board): 
    for list in board:
        if(0 in list):
            return board.index(list), list.index(0)

def getSolvedIndex(number):
    if(number == 0): return dim - 1, dim - 1
    return (number - 1) // dim, (number - 1) % dim 

def getHeuristicDistance(board):
    sum = 0
    for i in range(0, dim):
        for j in range(0, dim):
            fitx, fity = getSolvedIndex(board[i][j])
            sum += abs(fitx - i) + abs(fity - j)

    
    if(bothHeuristics): 
    #Both Manhattan distance and linear conflict
        linear_conflict1 = 0
        for i in range(dim):
            temp = -1
            for j in range(dim):
                cell_value = board[i][j]
                if (cell_value != 0) and ((cell_value - 1) / dim == i):
                    if cell_value > temp:
                        temp = cell_value
                    else:
                        linear_conflict1 += 2
                        
        linear_conflict2 = 0
        for j in range(dim):
            temp = -1
            for i in range(dim):
                cell_value = board[i][j]
                if (cell_value != 0) and (cell_value % dim == j + 1):
                        if cell_value > temp:
                            temp = cell_value
                        else:
                            linear_conflict2 += 2
                            
        return (sum + linear_conflict1 + linear_conflict2) * 1.36
    else: 
    #Only Manhattan distance heuristics
        return sum

def validCoord(x,y):
    return x >= 0 and y >= 0 and x < dim and y < dim

def moveZero(board, x, y):
    zerox, zeroy = getZeroPosition(board)
    board[x][y], board[zerox][zeroy] = board[zerox][zeroy], board[x][y]

def printBoard(currBoard):
    #print(currBoard)
    for a in range(0, dim):
        for b in range(0, dim):
            print(currBoard[a][b], end =" ")
        print("")

def solvable(puzzle):
    
    list_puzz = []
    for i in range(dim):
        list_puzz.append(puzzle[i])
        if 0 in puzzle[i] :
            blank = dim - i

    list_puzz = list(i for j in puzzle for i in j)
    inversions = 0

    for i in range(boardSize - 1):
        for j in range(i + 1, boardSize):
            if (list_puzz[i] != 0) and (list_puzz[j] != 0 ) and (list_puzz[j] < list_puzz[i]):
                inversions += 1
                
    if(dim % 2 != 0):
        return inversions % 2 == 0

    if (inversions + blank) % 2 != 0 :
        return True
    else:
        return False

bothHeuristics = False

dim = 3
boardSize = dim ** 2
board = []
visited = {}
numMoves = {}
solvedBoard = solved()

moves = [[-1,0],[1,0],[0,-1],[0,1]]

if(__name__ == "__main__"):
    
    toVisit = PriorityQueue()
        
    board = [[4, 3, 1], [5, 2, 8], [6, 7, 0]]
    #board = [[4, 3, 1], [5, 2, 8], [0, 7, 6]] # not solvable
    #board = [[1, 0 ,3], [4, 2, 5], [7, 8, 6]] # simple problem
    #board = [[1, 6 ,5], [7, 3, 8], [0, 4, 2]] # solvable problem 
    if(not solvable(board)):
        print("Not solvable")
        sys.exit()
    
    start = time.time()
    visited[str(board)] = False
    numMoves[str(board)] = 0
    toVisit.insert(deepcopy(board))
    board = 0
    diff = 0
    iter = 0
    while(not toVisit.isEmpty()):
        iter += 1
        board = toVisit.delete()

        diff = getHeuristicDistance(board)
        if(diff == 0):
            break

        for move in moves:
            newBoard = deepcopy(board)
            zerox, zeroy = getZeroPosition(board)
            if(validCoord( zerox + move[0] , zeroy + move[1])):
                moveZero(newBoard, zerox + move[0] , zeroy + move[1])
                #distance = getHeuristicDistance(newBoard)
                
                if( str(newBoard) not in visited.keys()):
                    toVisit.insert(newBoard)
                    visited[str(newBoard)] = str(board)
                    numMoves[str(newBoard)] = numMoves[str(board)] + 1
    
    boards = []
    board = str(board)
    while (board):
        boards.append(board)
        board = visited[board]
        
    boards.reverse()
        
    for board in boards:
        print(board)

    end = time.time()
    print("Vreme: ", end - start)
    #print("Number of iterations: " + str(iter))