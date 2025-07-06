# Simple 2-Player Congklak Game

This is a simple two-player *Congklak* (Mancala variant from Indonesia) game built using Python. Played via the command line, each player takes turns selecting a hole to distribute the seeds and tries to collect as many as possible in their store.

## 🎮 How to Play

- The board consists of 7 holes per player and 1 store (home) each.
- Players take turns picking one of their own holes (with seeds) to move.
- Seeds are distributed counter-clockwise, skipping the opponent's store.
- The game ends when all holes on one side are empty.
- Remaining seeds are collected into each player's store.
- The player with the most seeds in their store wins.

## 🧠 Game Rules Summary

- Each hole starts with 7 seeds.
- Valid moves: holes with seeds on your side (0-6).
- Skip your opponent's store when sowing.

## 🚀 How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/congklak_game.git
    cd congklak_game
    ```

2. Run the game:
    ```bash
    python congklak.py
    ```

> Make sure you have Python 3 installed.

