class TicTacToe:
    def __init__(self, board=[[0, 0, 0],
                             [0, 0, 0], 
                             [0, 0, 0]]):
        self.board = board

    def draw_board(self):
        print('  --- --- ---')
        Match = ['  |', ' O |', ' X |']
        for i in range(3):
            print('|', end='')
            for j in range(3):
                print(Match[self.board[i][j]], end='')
        print('\n  --- --- ---')
    
    # def player_one_move(self, p_row, p_colomn):
    #     self.board[[p_row][p_colomn]] = 1
    
    # def player_two_move(self, p_row, p_colomn):
    #     self.board[[p_row][p_colomn]] = 2


    # def check_full(self):
    #     for i in range(3):
    #         if 0 in self.board[i]:
    #             return False
    #     return True

    # def check_winner(self):
    #     player_one = False
    #     player_two = False
    #     #Diagonal
    #     if self.board[0][0] == self.board[1][1] == self.board[2][2]:
    #         if self.board[0][0] == 1:
    #             return "Player_1 WINS"
    #         elif self.board[0][0] == 2:
    #             return "Player_2 WINS"
    #     elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
    #         if self.board[0][0] == 1:
    #             return "Player_1 WINS"
    #         elif self.board[0][0] == 2:
    #             return "Player_2 WINS"
    #     #Row
    #     for i in range(3):
    #         row_element = set(self.board[i][0], self.board[i][1], self.board[i][2])
    #         if len(row_element) == 1:
    #             if 1 in row_element:
    #                 player_one = True
    #             if 2 in row_element:
    #                 player_two = True
    #     #Colomn
    #     for col in range(3):
    #         col_element = set(self.board[0][col], self.board[1][col], self.board[2][col])
    #         if len(col_element) == 1:
    #             if 1 in col_element:
    #                 player_one = True
    #             if 2 in col_element:
    #                 player_two = True
        
    #     if player_two == True and player_two == False:
    #         return 'player_1 WINS'
    #     if player_two == False and player_two == True:
    #         return 'player_2 WINS'
    #     # if player_two == False and player_two == False:
    #         # if :
    #         #     return 'Draw'
    #         # else :
    #         #     return 'Continue'

    # #Whole LOGIC OF THE GAME
    # def play_game(self):
    #     player = 1
    #     while True:
    #         if player == 1:
    #             row_index = int(input('P(layer 1 put Row:'))
    #             colomn_index = int(input('Player 1 put colomn'))
    #             self.player_one_move(row_index, colomn_index)
    #         else:
    #             row_index = int(input('P(layer 2 put Row:'))
    #             colomn_index = int(input('Player 2 put colomn'))
    #             self.player_two_move(row_index, colomn_index)
    #         self.draw_board()
    #         player = player % 2 + 1

    #         # win_condition = self.check_winner()
            
        
game = TicTacToe()
game.draw_board()