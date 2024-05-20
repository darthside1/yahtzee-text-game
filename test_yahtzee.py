import pytest
from yahtzee import YahtzeeGame, Dice

"""

IMPORTANT! Run pytest with '-s' flag to avoid stdin/output errors

"""

def test_is_yahtzee():
    dice = [Dice() for _ in range(5)]
    
    for die in dice:
        die.value = 6
    
    yahtzee_game = YahtzeeGame()
    yahtzee_game.dice_collection = dice
    
    assert yahtzee_game.is_yahtzee() is True


def test_not_yahtzee():
    dice = [Dice() for _ in range(5)]
    
    for die in dice:
        die.value = 6
    
    dice[0].value = 2
    
    yahtzee_game = YahtzeeGame()
    yahtzee_game.dice_collection = dice
    
    assert yahtzee_game.is_yahtzee() is False


def test_roll_is_unique():
    yahtzee_game = YahtzeeGame()
    initial_values = [die.value for die in yahtzee_game.dice_collection]
    
    yahtzee_game.roll_dice()
    new_values = [die.value for die in yahtzee_game.dice_collection]
    
    assert initial_values != new_values


if __name__ == '__main__':
    pytest.main()
