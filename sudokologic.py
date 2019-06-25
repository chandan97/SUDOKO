board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]

    ]




def boardprint():
    for i in range(9):
        if i%3==0 and i!=0:
            print("-------------------------")

        for j in range(9):
            if j%3==0 and j!=0:
                print("|" ,end ="")


            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ",end="")

def solution(board):
    get = findvacant(board)
    if not get:
        return True
    else:
        r,c = get
        


    for i in range(1,10):
        if validation(board,i,(r,c)):
            board[r][c] = i

            if solution(board):
                return True


            board[r][c] = 0

    return False


def validation(board,num,pos):
    #rowchecking
    for i in range(len(board[0])):
         if board[pos[0]][i] ==num and pos[1] != i:
            return False

    #columnchecking
    for i in range(len(board[0])):
            if board[i][pos[1]] == num and pos[0]!= i:
                return False



    boxx=pos[1] //3
    boxy = pos[0] // 3


    for i in range(boxy*3,boxy*3 +3):
        for j in range(boxx*3 , boxx*3 +3):
            if board[i][j] == num and (i,j) != pos:
                return False


    return True


def findvacant(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
           if board[i][j]==0:
               return (i,j)
                
    
    return None

boardprint()



   
