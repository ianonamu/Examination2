from Game.player import DicePlayer
from Game.dicehand import Game.dice

class Intelligence:
    """Class representing the intelligence of the computer."""

    def __init__(self):
        self.dicehand = Dicehand()
        self.player = Player()
        self.name = "Computer"
        self.computer_score = 0
        self.computer_total = []
        self.computer_hold_once = True
        self.player_score = self.player.get_score()
        self.computer_current = 0

    def easy(self):
        if self.computer_hold_once:
            print("\nComputer chose to roll")
            self.computer_current = self.dicehand.dice_roll()
            if self.computer_current == 1:
                self.computer_score = 0
                self.computer_total = []
                print("OOPS! The computer rolled a 1, so it PIGs out!")
                self.computer_hold_once = False
            else:
                self.computer_rolls(self.computer_current)
            self.display_computer_score(self.computer_current, self.computer_score)
            self.computer_hold_once = False
            return self.computer_score
        elif not self.computer_hold_once or self.computer_score > 25:
            print("\nComputer chose to hold")
            print("Computer's Updated Scores:")
            self.computer_score = self.update_computer_score(0)
            self.computer_current = 0
            self.display_computer_score(self.computer_current, self.computer_score)
            self.computer_hold_once = True
            if self.computer_score is None:
                self.computer_score = 0
            return self.computer_score
        else:
            return self.computer_score

    def medium(self):
        if self.computer_hold_once:
            print("\nComputer chose to roll")
            self.computer_current = self.dicehand.dice_roll()
            if self.computer_current == 1:
                self.computer_score = 0
                self.computer_total = []
                print("OOPS! The computer rolled a 1, so it PIGs out!")
                self.computer_hold_once = False
            else:
                self.computer_rolls(self.computer_current)
            self.display_computer_score(self.computer_current, self.computer_score)
            self.computer_hold_once = False
            return self.computer_score
        elif not self.computer_hold_once or self.computer_score > 20:
            print("\nComputer chose to hold")
            print("Computer's Updated Scores:")
            self.computer_score = self.update_computer_score(0)
            self.computer_current = 0
            self.display_computer_score(self.computer_current, self.computer_score)
            self.computer_hold_once = True
            if self.computer_score is None:
                self.computer_score = 0
            return self.computer_score
        else:
            return self.computer_score

    def hard(self):
        if self.computer_hold_once:
            print("\nComputer chose to roll")
            self.computer_current = self.dicehand.dice_roll()
            if self.computer_current == 1:
                self.computer_score = 0
                self.computer_total = []
                print("OOPS! The computer rolled a 1, so it PIGs out!")
                self.computer_hold_once = False
            else:
                self.computer_rolls(self.computer_current)
            self.display_computer_score(self.computer_current, self.computer_score)
            self.computer_hold_once = False
            return self.computer_score
        elif not self.computer_hold_once or self.computer_score > 15:
            print("\nComputer chose to hold")
            print("Computer's Updated Scores:")
            self.computer_score = self.update_computer_score(0)
            self.computer_current = 0
            self.display_computer_score(self.computer_current, self.computer_score)
            self.computer_hold_once = True
            if self.computer_score is None:
                self.computer_score = 0
            return self.computer_score
        else:
            return self.computer_score

    def computer_rolls(self, computer_roll):
        self.computer_total.append(computer_roll)
        return self.computer_total

    def update_computer_score(self, computer_rolls):
        computer_rolls = sum(self.computer_rolls(0))
        self.computer_score = computer_rolls
        return self.computer_score

    def get_computer_score(self):
        return self.computer_score

    def get_computer_current(self):
        return self.computer_current

    def display_computer_score(self, current_computer_score, computer_score):
        print(
            f"Computer's Current score: {current_computer_score}\nComputer's Total score: {computer_score}"