# TicTacToe-Task

# Tic Tac Toe Game in Python with NumPy: A Battle of Wits! 🎲🧠
## Introduction 🌟 
Three days ago I had a programming assignment, which was to write a code for the Sudoku game (by the way, it's my favorite game since childhood). At first, I came up with a logical solution for the game, and then I started with the programming solution. The people who gave me the assignment advised me to write the code using Python, but my stubbornness led me to decide to use Java! Of course, I couldn't, hahaha, and I turned to Python and was able to solve it later. Today, with the Tuwaiq Academy assignment in Artificial Intelligence Bootcamp, the goal is to write code for the Tic Tac Toe game using the Numpy library. I found a great similarity after looking closely at the Sudoku code I wrote a few days ago. Isn't Sudoku the Tic Tac Toe game, but it's repeated 9 times? So why don't I use the same logic?


## Game Rules 📜
Here are the fundamental rules that govern this timeless game:
- **Objective:** The goal is to form a line (horizontal, vertical, or diagonal) with your symbol (either 'X' or 'O') before your opponent does.
- **Game Board:** The game board consists of a 3x3 grid, like a tic-tac-toe notebook.
- **Players:** The game is typically played by two players, one using 'X' and the other 'O'. You can decide who plays which symbol.
- **Taking Turns:** Players take turns to place their symbol on an empty cell on the grid.
- **Winning:** The first player to form a line with their symbol wins the game. If the grid is full and no one has formed a line, the game is a draw (a "cat's game").
- **Game Flow:** The game starts with an empty grid. Players take turns until there's a winner.
## Task Checklist 📋
Here's a step-by-step breakdown of your task:
1. **Game Board Setup:** Create a 3x3 grid for the game board. You can use a NumPy array for this.
2. **Player Input:** Implement a way for players to input their moves. Ensure that the input is valid (e.g., within the grid and not on an already occupied cell).
3. **Game Logic:** Develop the logic to check for a win or a draw after each move. If there's a winner, declare the winner. If the game ends in a draw, announce the draw.
4. **Game Loop:** Design a loop that allows players to take turns until there's a winner or a draw.
5. **Player vs. Player:** Implement a two-player mode where two human players can take turns to play.
