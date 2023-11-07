import random


class GuessingGame:
    def __init__(self) -> None:
        self.low = None
        self.high = None
        self.tries = 3
        self.very_high_diff = (20, "very high")
        self.high_diff = (10, "high")
        self.low_diff = (6, "low")
        self.very_low_diff = (3, "very low")
        self.diff = None
        self.indicator_msg = None
    
    def set_limits(self, low_limit, high_limit):
        self.low = low_limit
        self.high = high_limit

    def ask_for_limits(self):
        while True:
            l_limit = input("Provide a low limit: ")
            h_limit = input("Provide a high limit: ")
            try:
                l_limit, h_limit = int(l_limit), int(h_limit)
            except ValueError:
                print("Only integers allowed as limits.")
                continue
            if l_limit == h_limit:
                print("Limits can't be same number. Provide new ones.")
                continue
            elif l_limit > h_limit:
                print("Low limit can't be greater than high limit. Provide new ones.")
                continue
            self.set_limits(l_limit, h_limit)
            break

    def guess(self):
        print(f"""
        --------------------------------
            these are your limits:
            {self.low} - {self.high}
        --------------------------------\n\n
        """)
        answer = random.randint(self.low, self.high)
        
        while True:
            u_guess = input("Your guess: ")
            self.tries -= 1
            try:
                u_guess = int(u_guess)
            except ValueError:
                if self.tries == 0:
                    print(f"You lost! Answer = {answer}")
                    break
                print(f"Only integers. Provide new guess. Tries left {self.tries}")
                continue
            if u_guess == answer:
                print("You're correct!")
                break
            else:
                if self.tries != 0:
                    if u_guess > self.high:
                        self.diff = abs(u_guess - self.high)
                        print(f"Really, this is even higher that your high limit. Tries left {self.tries}")
                        continue
                    elif u_guess < self.low:
                        print(f"Really, this is even lower that your low limit. Tries left {self.tries}")
                        continue
                    elif u_guess > answer:
                        print(f"Incorrect, high! tries left {self.tries}")
                        continue
                    elif u_guess < answer:
                        print(f"Incorrect, low! tries left {self.tries}")
                        continue
                else:
                    print(f"You lost! Answer = {answer}")
                    break

    def get_diff_msg(self):
        msg = ""
        if self.diff >= self.very_high_diff[0]:
            msg = self.very_high_diff[1]
        elif self.diff >= self.high_diff[0]:
            msg = self.high_diff[1]
        elif self.diff >= self.low_diff[0]:
            msg = self.low_diff[1]
        elif self.diff <= self.very_low_diff[0]:
            msg = self.very_low_diff[1]
        self.indicator_msg = msg
        
    def start(self):
        self.print_welcome_message()
        self.ask_for_limits()
        self.guess()

    def print_welcome_message(self):
        message = """
        |---------------------------------------------------|
        |                                                   |
        |                                                   |
        |              Guessing Game                        |
        |                                                   |
        |                                                   |
        |---------------------------------------------------|

        The only rule:

        1. You have 3 tries to guess the correct number.

        """
        print(message)


def main():
    game = GuessingGame()
    game.start()


if __name__ == "__main__":
    main()
