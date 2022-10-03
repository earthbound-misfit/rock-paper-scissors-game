import random

class RockPaperScissors():
    def __init__(self, computer_choice=None, player_choice=None):
        self.computer_choice = computer_choice
        self.player_choice = player_choice
    
    def generate_player_choice(self):
        self.player_choice = input('Type "Rock", "Paper", or "Scissors": ')
        return self.player_choice

    def generate_computer_choice(self):
        self.computer_choice = random.choice(['rock','paper','scissors'])
        return self.computer_choice


def Play(self):
    while True:
        user_response_required = input('Type "P" to Play, or "Q" to Quit: ')

        if user_response_required.lower() == 'q':
            print('Thanks for playing Rock-Paper-Scissors!')
            break 
        else:
            print("Welcome to Rock-Paper-Scissors! Let's play!!! ")
            self.player_choice = self.generate_player_choice()
            self.computer_choice = self.generate_computer_choice()
            print(f'Your opponent has chosen: {self.computer_choice.title()}')
            if self.player_choice.lower() == 'rock':
                if self.computer_choice == 'paper':
                    print(f'You lose!')
                elif self.computer_choice == 'scissors':
                    print(f'You win!')
                else:
                    print(f"It's a tie!")
            elif self.player_choice.lower() == 'paper':
                if self.computer_choice == 'scissors':
                    print(f'You lose!')
                elif self.computer_choice == 'rock':
                    print(f'You lose!')
                else:
                    print(f"It's a tie!")
            elif self.player_choice.lower() == 'scissors':
                if self.computer_choice == 'rock':
                    print(f'You lose!')
                elif self.computer_choice == 'paper':
                    print(f'You win!')
                else:
                    print(f"It's a tie!")


new = RockPaperScissors()

Play(new)


