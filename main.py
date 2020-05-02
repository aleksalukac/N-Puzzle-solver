from copy import deepcopy
import time

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

    return sum

def validCoord(x,y):
    return x >= 0 and y >= 0 and x < dim and y < dim

def moveZero(board, x, y):
    zerox, zeroy = getZeroPosition(board)
    board[x][y], board[zerox][zeroy] = board[zerox][zeroy], board[x][y]

dim = 3
boardSize = dim ** 2
board = []
solvedBoard = solved()

moves = [[-1,0],[1,0],[0,-1],[0,1]]

if(__name__ == "__main__"):
    
    visited = {}
    toVisit = PriorityQueue()
        
    board = [[4, 3, 1], [5, 2, 8], [6, 7, 0]]

    start = time.time()
    visited[str(board)] = False
    toVisit.insert(deepcopy(board))
    board = 0
    diff = 0
    iter = 0
    while(not toVisit.isEmpty()):
        iter += 1
        board = toVisit.delete()

        diff = getHeuristicDistance(board)
        if(diff == 0):
            print(diff)
            print(board)
            print("-" * 33)
            break

        for move in moves:
            newBoard = deepcopy(board)
            zerox, zeroy = getZeroPosition(board)
            if(validCoord( zerox + move[0] , zeroy + move[1])):
                moveZero(newBoard, zerox + move[0] , zeroy + move[1])
                distance = getHeuristicDistance(newBoard)
                
                if( str(newBoard) not in visited.keys()):
                    toVisit.insert(newBoard)
                    visited[str(newBoard)] = str(board)
    
    board = str(board)
    while (board):
        print(board)
        board = visited[board]

    end = time.time()
    print("Vreme: ", end - start)
    #print("Number of iterations: " + str(iter))
