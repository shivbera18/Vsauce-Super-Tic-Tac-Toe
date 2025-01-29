# Super Tic-Tac-Toe

Inspired by a YouTube shorts from Vsauce  
[https://youtube.com/shorts/\_Na3a1ZrX7c?si=2uSyEbpub4_PB3SS]

An improved and more fun version of the classic but lame Tic-Tac-Toe game

## Rules

Super Tic-Tac-Toe is played on a 3x3 grid of smaller 3x3 boards. The goal is to win three small boards in a sequence on the super board.

1. **Objective**: Win three small boards in a sequence on the super board (horizontal, vertical, or diagonal).
2. **Turns**: Players take turns placing O or X on a small board.
   - Each move sends the opponent to a specific small board based on the cell played (e.g., top-left sends to top-left).
   - If directed to a full or won board, the opponent may play anywhere.
3. **Winning**:
   - Win a small board by making three in a row within it.
   - Win the game by winning three small boards in a sequence on the super board.
4. **Draw**: If all boards fill without a winner, the game is a draw.

## Installation

First **pip install numpy** if you haven't already

```bash
pip install numpy
```

To set up Super Tic-Tac-Toe on your local machine

**Clone the repository** to your local machine:

```bash
git clone https://github.com/yourusername/super_tictactoe.git
```

**Navigate to the project directory**:

```bash
cd super_tictactoe
```

**Run main.py** and enjoy the game!

```bash
python main.py
```

## License

MIT License
