import random


class Dice:
    def __init__(self):
        self.roll()

    def roll(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return f"Dice shows {self.value}"


class YahtzeeGame:
    def __init__(self):
        self.dice_collection = [Dice() for _ in range(5)]
        self.max_rolls = 3
        self.keep_playing = True
        self.play()


    def play(self):
        while self.keep_playing:
            print("Welcome to Yahtzee!")
            for roll_num in range(self.max_rolls):
                print(f"Starting turn: {roll_num + 1} of {self.max_rolls}, rolling dice")
                self.roll_dice()
                print(f"\n".join(str(i) + ": " + str(die) for i, die in enumerate(self.dice_collection)))

                if self.is_yahtzee():
                    print(f"YAHTZEE with {self.dice_collection[0].value}'s!")
                    break

                if roll_num < self.max_rolls - 1:
                    if not self.ask_to_roll_again():
                        self.keep_playing = False
                        break
            else:
                self.keep_playing = self.ask_to_play_again()


    def roll_dice(self):
        for die in self.dice_collection:
            die.roll()


    def is_yahtzee(self):
        first_value = self.dice_collection[0].value
        return all(die.value == first_value for die in self.dice_collection)


    def ask_to_roll_again(self):
        return input("Want to throw again? (y for yes, anything else for no) ").strip().lower() == 'y'


    def ask_to_play_again(self):
        return input("Game over! Want to play again? ").strip().lower() == 'y'
    

if __name__ == '__main__':
    YahtzeeGame()
