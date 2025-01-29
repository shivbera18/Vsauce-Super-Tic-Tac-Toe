import numpy as np

def display_board(current):
    """
    prints the current borad state
    Parameters:
    current (numpy.ndarray): current board state with shape (9,9)
    Returns:
    None
    """
    assert current.shape == (9,9), "current must be of shape (9,9)"

    for i in range(3):
        for j in range(3):
            print(f'{current[3*i][3*j]}|{current[3*i][3*j+1]}|{current[3*i][3*j+2]}', end="  ")
            print(f'{current[3*i+1][3*j]}|{current[3*i+1][3*j+1]}|{current[3*i+1][3*j+2]}', end="  ")
            print(f'{current[3*i+2][3*j]}|{current[3*i+2][3*j+1]}|{current[3*i+2][3*j+2]}')
        print("")
    print("-"*18)
    print("")

class TicTacToe:
    def __init__(self):
        self.board = np.full(9, " ")

    def __getitem__(self, index):
        return self.board[index]

    def display(self):
        for i in range(3):
            print(f'{self.board[3*i]}|{self.board[3*i+1]}|{self.board[3*i+2]}')

    def check_win(self):
        for i in range(3):
            if self.board[3*i] == self.board[3*i+1] == self.board[3*i+2] != " ":
                return True
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True

        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True

        return False

    def check_draw(self):
        for i in range(9):
            if self.board[i] == " ":
                return False
        return True

    def play(self, player, play):
        """
        Updates the TicTacToe game state by placing a player's mark at a specified position on the board.
        Parameters:
            player (str): The mark of the player making the move (e.g., 'X' or 'O').
            play (int): The position on the board where the player's mark will be placed.
        Returns:
            None
        """
        self.board[play] = player

class SuperTicTacToe():
    def __init__(self):
        self.board = [TicTacToe() for _ in range(9)]
        self.meta_board = np.full(9, " ")
        self.next_board = -1

    def display(self):
        arrays = []
        for i in self.board:
            arrays.append(i.board)
        stack = np.vstack(arrays)
        display_board(stack)

    def check_win(self):
        for i in range(3):
            if self.meta_board[3*i] == self.meta_board[3*i+1] == self.meta_board[3*i+2] != " ":
                return True
            if self.meta_board[i] == self.meta_board[i+3] == self.meta_board[i+6] != " ":
                return True

        if self.meta_board[0] == self.meta_board[4] == self.meta_board[8] != " ":
            return True
        if self.meta_board[2] == self.meta_board[4] == self.meta_board[6] != " ":
            return True

        return False

    def check_draw(self):
        for i in range(9):
            if self.meta_board[i] == " ":
                return False
        return True
    
    def get_valid_move(self, player):
        while True:
            try:
                play = input(f"Player '{player}', enter position (row,col from 1-9): ")
                row, col = map(int, play.split(","))
                row -= 1
                col -= 1
                
                # Validate input range
                if not (0 <= row <= 8 and 0 <= col <= 8):
                    print("Position must be between 1 and 9")
                    continue

                # Validate next board
                if self.next_board != -1 and self.next_board != row: #and self.meta_board[row] != " "
                    print(f"Play in board {self.next_board + 1}")
                    continue
                
                # Validate empty position
                if self.board[row][col] != " ":
                    print(f"Position {row+1},{col+1} is already occupied")
                    continue
                    
                return row, col
                
            except ValueError:
                print("Invalid input format. Example: 2,4") 

    def play(self):
        self.display() 
        player = "O"
        while True:
            a, b = self.get_valid_move(player) 
            
            mini_board = self.board[a]
            mini_board.play(player, b)

            if mini_board.check_win():
                self.meta_board[a] = player
                mini_board.board = np.full(9, player)
            elif mini_board.check_draw():
                self.meta_board[a] = "D"
                mini_board.board = np.full(9, "D")
                
            self.next_board = b if self.meta_board[b] == ' ' else -1

            if self.check_win():
                self.display() 
                print(f"player '{player}' won the game!") 
                break
            
            if self.check_draw():
                self.display() 
                print("Draw") 
                break

            player = "O" if player == "X" else "X"
            
            self.display() 
            