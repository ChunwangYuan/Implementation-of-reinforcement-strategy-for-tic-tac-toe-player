#created board with flexbile board size, reset board,

class Board():
    def __init__(self, board_size):
        self.board_size= board_size
        self.board = self.reset_board()

    def reset_board(self):
        self.board= []
        for i in range(self.board_size):
            self.board.append([])
            for j in range(self.board_size):
                self.board[i].append(None)

        return self.board

    def get_available_moves(self):
        available_moves=[]

    def print_board(self):
        for i in range(self.board_size):
            print(' \n')
            for j in range(self.board_size):
                print(self.board[i][j], end=' \t')

    def available_moves(self):
        available_moves=[]
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == None:
                    available_moves.append((i, j))
        return available_moves

    def move(self, position, value):
        self.board[position[0]][position[1]] = value


    def game_result(self):
        for i in range(self.board_size):
            if len(set(self.board[i]))==1 and self.board[i][0]!= None:
                return self.board[i][0]


        for i in range(self.board_size):
            column_list = []
            for j in range(self.board_size):
                column_list.append(self.board[j][i])
            if len(set(column_list))==1 and self.board[j][i]!= None:
                return column_list[0]


        #diagonal'
        column_list = []
        for i in range(self.board_size):
            column_list.append(self.board[i][i])
        if len(set(column_list))==1 and self.board[0][0]!= None:
            return column_list[0]


        diagonal = []
        for i in range(len(self.board)):
            diagonal.append(self.board[i][len(self.board) - i - 1])
        if len(set(diagonal)) == 1 and self.board[0][2] != None:
            return self.board[0][2]

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == None:
                    return 'Game_not_ended'









if __name__== '__main__':
    b1= Board(3)
    a=b1.reset_board()
    # b1.print_board()
    c1=b1.available_moves()
    print('c1',c1)
    v1=b1.move((0,0),'x')
    v1=b1.move((0,1),'x')
    v1=b1.move((1,1),'x')
    v1=b1.move((2,0),'x')

    b1.print_board()
    j1=b1.game_result()
    print('\n',j1)




