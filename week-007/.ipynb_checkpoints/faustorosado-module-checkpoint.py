from random import randint


sides = [0, 1]

class Coin:
    
    def __init__(self):
        #self.start = 0
    
        
    def flip(self):
        self.start = sides[randint(0,1)]
        return self.start

    

    def game(self):
        while True:
            guess = input("0 for heads or 1 for tails? ")
            flip = coin.flip()
            if flip == int(guess):
                print(f"Way to go")
            else:
                print(f"Try again")
    
    
    


if __name__ == '__main__':
    coin = Coin()
    coin.game()