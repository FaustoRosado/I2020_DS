import random

class RockPaperScissor:
    def __init__(self, rounds=3):
        self.rounds = rounds
        
    @staticmethod
    def welcome():
        print("Rock, Paper, Scissors")
        
    def computers_turn(self):
        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissors'
        }
        turn = random.randint(0,2)
        return (turn, choices[turn])
    
    def your_turn(self, choice):
        if choice not in ['r', 'p', 's']:
            raise ValueError("Must be r - rock, p - paper, s - scissors")

        choices = {
            'r': (0, 'rock'),
            'p': (1, 'paper'),
            's': (2, 'scissors'),
        }    
        return choices[choice] 

    def compare_turns(self,user_choice, computer_choice):
        results = {
            0: 'tie',
            1: 'You win',
            2: 'Computer wins, you loose'
        }
        k = (user_choice[0] - computer_choice[0]) % 3
        return results[k]
                
    def won_round(self):
        user_input = input("Choose r - rock , p - paper, or s - scissors: ")
        computer_choice = self.computers_turn()
        print(f"{computer_choice} is computer choice")
        user_choice = self.your_turn(user_input)
        print(f"{user_choice} is your choice'")
        return self.compare_turns(user_choice, computer_choice)
        
    def run(self):
        RockPaperScissor.welcome()
        print('running')
        count = int(self.rounds)
        while count > 0:
            w = self.won_round()
            print(w)
            count -=1
            print(f"{count} turns left")
           
    
if __name__ == '__main__':
    rps = RockPaperScissor()
    rps.run()