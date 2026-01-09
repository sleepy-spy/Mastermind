import random


class Mastermind:  # Make the code, validate the guesses
    def __init__(self, turns=10):
        self.max_turns = turns
        self.turns_taken = 0
        self.failed = False
        self.code = ""
        self.guess = ""
        self.feedback = ""
        self.beaten = False

    def generate_code(self):
        digits = random.sample(range(0, 10), 4)
        self.code = "".join(map(str, digits))

    def guess_code(self):
        self.guess = input(f"Turn {self.turns_taken + 1}: Please input your 4 digit code guess: ")
        while len(self.guess) != 4:
            self.guess = input(
                f"Turn {self.turns_taken + 1}: Please input your 4 digit code guess. Digits from 0-9 Only!"
            )
        self.turns_taken += 1

    def evaluate_code(self):
        unused_code = []
        unused_guess = []
        if self.guess == self.code:
            self.beaten = True
        else:
            for i in range(4):
                if self.guess[i] == self.code[i]:
                    self.feedback += "R"
                else:
                    unused_code.append(str(self.code[i]))
                    unused_guess.append(str(self.guess[i]))
            for number in unused_guess:
                if number in unused_code:
                    self.feedback += "W"
                    unused_code.remove(number)
            print(self.feedback)
            self.feedback = ""
    



            



def main():
    max_turns = int(input("Please input the max number of guesses you wish to use. Numbers only!: "))
    game = Mastermind(turns=max_turns)
    game.generate_code()
    game.code = "8519"
    while not game.beaten and game.turns_taken < game.max_turns:
        game.guess_code()
        game.evaluate_code()
    if game.turns_taken == game.max_turns and game.guess != game.code:
        print(f"You have failed to guess the code. The code is {game.code}")
    else:
        print("You have successfully guessed the code!")

if __name__ == "__main__":
    main()
    
