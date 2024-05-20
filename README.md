# Written by

Patryk Robakowski

# Yahtzee Game

A simple implementation of the classic Yahtzee game in Python.

## Files

### yahtzee.py

This file contains the main logic for the Yahtzee game, including the `Dice` and `YahtzeeGame` classes.

#### `Dice` Class
- `__init__(self)`: Initializes the dice and rolls it.
- `roll(self)`: Rolls the dice, generating a random value between 1 and 6.
- `__str__(self)`: Returns a string representation of the dice's value.

#### `YahtzeeGame` Class
- `__init__(self)`: Initializes the game with a set of 5 dice, sets the maximum number of rolls per turn to 3, and starts the game.
- `play(self)`: Main game loop where the player can roll dice, check for Yahtzee, and decide to roll again or end the game.
- `roll_dice(self)`: Rolls all dice in the collection.
- `is_yahtzee(self)`: Checks if all dice in the collection have the same value.
- `ask_to_roll_again(self)`: Prompts the player to decide if they want to roll again.
- `ask_to_play_again(self)`: Prompts the player to decide if they want to play another game.

### test_yahtzee.py

This file contains unit tests for the Yahtzee game using `pytest`.

#### Tests
- `test_is_yahtzee()`: Verifies that the `is_yahtzee` method correctly identifies a Yahtzee when all dice values match.
- `test_not_yahtzee()`: Verifies that the `is_yahtzee` method correctly identifies when the dice values do not match.
- `test_roll_is_unique()`: Ensures that rolling the dice changes their values.

### Important Note
When running the tests, use the `-s` flag with `pytest` to avoid stdin/output errors:
```sh
pytest -s
```

## How to Run

1. **Play the Game**:

`Windows`:
   ```sh
   python yahtzee.py -s
   ```
`MacOS`:
   ```sh
   python3 yahtzee.py -s
   ```

2. **Run the Tests**:

   ```sh
   pytest -s
   ```

## Requirements

- Python 3.x
- `pytest` for running the tests

## Installation

1. Clone the repository.
2. Navigate to the directory containing the files.
3. Install `pytest` if not already installed:
`Windows`:
   ```sh
   pip install pytest
   ```
`MacOS`:
   ```sh
   pip3 install pytest
   ```
## Usage

To play the game, simply run `yahtzee.py`. Follow the on-screen prompts to roll the dice and decide whether to roll again or end the game.

To run the tests, use `pytest -s` to ensure all input and output operations work correctly.

Enjoy playing Yahtzee!
```