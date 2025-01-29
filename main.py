from engine import SuperTicTacToe
from ai import MonteCarloAI

def main():
    ask = input("Play with Monte Carlo AI? (y/n): ")
    
    if ask == 'y' or ask == 'Y':
        strength = input("Enter AI strength (easy, medium, hard): ")
        if strength == 'easy':
            iter = 10
        elif strength == 'medium':
            iter = 100
        else:
            iter = 500

        game = MonteCarloAI(iter)
        game.play()
    else:
        game = SuperTicTacToe()
        game.play()

if __name__ == '__main__':
    main()