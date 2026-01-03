import random

class Mastermind: # Make the code, validate the guesses
    def __init__(self):
        self.max_turns = 0
        self.turns_taken = 0
        self.code = ""
        self.guess = ""

    def generate_code(self):
        digits = random.sample(range(0, 10), 4)
        self.code = "".join(map(str, digits))

    def guess_code(self):
        self.guess = input("Please input your 4 digit code guess")
        while len(self.guess) != 4:
            self.guess = input("Please input your 4 digit code guess. Digits from 0-9 Only!")

    def evaluate_code(self):
        for i in range(4):
            ...



def main():
    ...
