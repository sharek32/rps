# rps
# Rock Paper Scissors AI Player

This repository contains an adaptive AI player for the classic Rock, Paper, Scissors game.

## Overview

The `player` function in `RPS.py` analyzes the opponent's move history to predict their next move. It employs multiple strategies including frequency analysis, cycle detection, and reactive play to counter different types of bots effectively.

## Features

- Tracks opponent's previous moves to detect patterns.
- Adapts strategy dynamically to maximize win rate.
- Specifically designed to beat multiple predefined bot strategies with a win rate of at least 60%.

## Usage

The `player` function takes the opponent's previous move as input and returns the AI's next move (`"R"`, `"P"`, or `"S"`). It maintains state internally between calls.

---

*This solution is developed for the freeCodeCamp Rock Paper Scissors challenge.*
