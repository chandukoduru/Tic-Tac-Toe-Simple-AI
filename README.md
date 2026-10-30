# Tic-Tac-Toe with Simple AI

A terminal-based Tic-Tac-Toe game where a human plays as **X** against the computer as **O**. The computer uses the Minimax algorithm to select strong moves.

## Features
- 3x3 game board.
- Human-versus-computer gameplay.
- Minimax AI opponent.
- Input validation for invalid or occupied positions.
- Correct win, loss, and draw detection.
- Board is displayed after every move.

## Requirements
- Python 3.8 or later
- No external packages required

## Run
```bash
python main.py
```

## How to play
1. Run the program.
2. You play as `X`; the computer plays as `O`.
3. Enter a position from 1 to 9 when prompted.
4. The game ends when a player wins or the board is full.

## Position guide
```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## AI explanation
Minimax explores the possible moves from the current board. It gives the computer a positive score for a win, a negative score for a human win, and zero for a draw. The computer chooses the move with the best score.
