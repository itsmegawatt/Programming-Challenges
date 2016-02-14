import random

class Number_Guessing_Game(object):
    def __init__(self):
        self.minimum_number = 0
        self.maximum_number = 100
        self.guesses = 0
        self.maximum_guesses = 10

        self.game()

    def game(self):
        correct_number = random.randint(self.minimum_number, self.maximum_number)
        guessed_number = None
        print("I'm thinking of a number between {} and {}. You have {} attempts to figure it out.").format(self.minimum_number, self.maximum_number, self.maximum_guesses)
        while self.guesses < self.maximum_guesses and correct_number != guessed_number:
            guessed_number = int(input('Guess a number: '))
            self.guesses += 1
            if guessed_number == correct_number:
                print("You got it! {} is the right answer!".format(correct_number))
            if guessed_number < correct_number:
                print("Too low.")
            if guessed_number > correct_number:
                print("Too high.")
            print("Attempts so far: {}").format(self.guesses)
        print("Game Over.")

if __name__ == "__main__":
    new_game = Number_Guessing_Game()
