import numpy as np
import random
import math
from copy import deepcopy
from engine import SuperTicTacToe

class MonteCarloAI(SuperTicTacToe):
    def __init__(self, iter=10):    
        """
        Play with a Monte Carlo AI player for the Super TicTacToe game.
        
        Parameters:
            iter (int): The number of iterations for the Monte Carlo simulation.

        """
        super().__init__()
        self.iter = iter

    def get_best_move(self, player):
        """
        Returns the best move based on Monte Carlo simulation results
        Returns: tuple (row, col) representing the best move
        """
        available_moves = [(self.next_board,i) for i in range(9) if self.next_board != -1 and self.board[self.next_board].board[i] == " "]
        if self.next_board == -1:
            print('here')
            available_moves = [(i,j) for i in range(9) for j in range(9) if self.meta_board[i] == " " and self.board[i].board[j] == " "]

        # store wins and total simulations for each possible move
        wins = {move: 0 for move in available_moves}
        sims = {move: 0 for move in available_moves}

        for move in available_moves:
            for _ in range(self.iter):
                board_copy = deepcopy(self.board)
                meta_board_copy = deepcopy(self.meta_board)
                next_board_copy = deepcopy(self.next_board)

                board_copy[move[0]].board[move[1]] = player

                temp_game = MonteCarloAI()
                temp_game.board = board_copy
                temp_game.meta_board = meta_board_copy
                temp_game.next_board = next_board_copy
                result = temp_game._simulate_game(player)

                if result == player:
                    wins[move] += 1
                sims[move] += 1

        move_win_rates = {move: wins[move]/sims[move] for move in available_moves}

        return max(move_win_rates, key=move_win_rates.get)

    def _simulate_game(self, player):
        """
        Simulates a random game from the current position until completion
        Returns the winner ('X', 'O', or 'Draw')
        """
        while True:
            if self.check_win():
                return player
            if self.check_draw():
                return "Draw"
            
            # Get valid moves for current board state
            valid_moves = []
            if self.next_board == -1:  # Can play anywhere
                for i in range(9):
                    if self.meta_board[i] == ' ':  # If sub-board isn't won
                        for j in range(9):
                            if self.board[i].board[j] == ' ':
                                valid_moves.append((i, j))
            
            else:  # Must play in specific sub-board
                if self.meta_board[self.next_board] == ' ':  # If sub-board isn't won
                    for j in range(9):
                        if self.board[self.next_board].board[j] == ' ':
                            valid_moves.append((self.next_board, j))
                else:  # If forced board is full/won, can play anywhere
                    for i in range(9):
                        if self.meta_board[i] == ' ':
                            for j in range(9):
                                if self.board[i].board[j] == ' ':
                                    valid_moves.append((i, j))

            if not valid_moves:
                return "Draw"
            
            # Make random move
            player = "O" if player == "X" else "X"
            move = random.choice(valid_moves)
            self.board[move[0]].board[move[1]] = player

            # Update meta board if sub-board was won
            sub_board_winner = self.board[move[0]].check_win()
            if sub_board_winner:
                self.meta_board[move[0]] = player
            elif self.board[move[0]].check_draw():
                self.meta_board[move[0]] = 'D'
                
            # Update next board
            self.next_board = move[1] if self.meta_board[move[1]] == ' ' else -1
            
    def play(self):
        self.display() 
        player = "O"
        
        while True:
            if player == "O":
                if self.next_board == -1:
                    print(f'you can place anywhere')
                else:
                    print(f'place in board {self.next_board + 1}')
                a, b = self.get_valid_move(player) 
            else:
                a, b = self.get_best_move(player)
            
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