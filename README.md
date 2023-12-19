# U.S. States Guessing Game
This simple Python game allows users to guess the names of the 50 U.S. states. The game utilizes the Turtle graphics library to display an image of the U.S. map with the states' outlines. The objective is to guess the names of the states by typing them in when prompted.

## How to Play

1. Run the game script in a Python environment.
2. A window will appear with a blank map of the U.S. and a prompt asking for the name of a state.
3. Type the name of a U.S. state and press Enter.
4. If the guess is correct, the state name will be displayed on the map, and the game will prompt for the next guess.
5. Continue guessing until you correctly identify all 50 states or type 'Exit' to end the game.
6. After the game ends, a CSV file named `states_to_learn.csv` will be created, listing the states you still need to learn.

## Dependencies

- Python 3.x
- Turtle graphics library
- Pandas library

## Setup

1. Install Python if not already installed: [Python Download](https://www.python.org/downloads/).
2. Install the required libraries using the following command:
   ```bash
   pip install pandas
