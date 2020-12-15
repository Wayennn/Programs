from random import shuffle

class Card():
    values = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    suits = [None, "Clubs", "Hearts", "Diamonds", "Spades"]
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]
    def __add__(self, other):
        self.value + other.value

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(1, 11):
            for j in range(1, 5):
                self.cards.append(Card(i, j))
        shuffle(self.cards)
    def pick_card(self):
        if len(self.cards)==0:
            return None
        else:
            return self.cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.hand = []
        self.handval = 0
    def print_hand(self):
        hnd = []
        for i in range(len(self.hand)):
            hnd.append(str(self.hand[i]))
        print(self.name + "'s cards are " + " and ".join(hnd) + ".")
    def hand_value(self):
        self.hand_val = 0
        a = len(self.hand)
        for i in range(len(self.hand)):
            if self.hand[i].value!=1:
                self.hand_val += self.hand[i].value
                a -= 1
        for i in range(a-1, -1, -1):
            if (self.hand_val+11*(i+1))<=21:
                self.hand_val += 11
            else:
                self.hand_val += 1
        print(self.name + "'s hand value is " + str(self.hand_val))

class Game():
    def __init__(self):
        self.player1 = Player(input("Input player name: "))
        self.cpu = Player("CPU")
        self.deck = Deck()

    def play_game(self):
        while True:
            for i in range(2):
                self.player1.hand.append(self.deck.pick_card())
            for i in range(2):
                self.cpu.hand.append(self.deck.pick_card())
            self.player1.print_hand()
            hirit = input("Press \"e\" to pick one more card ").lower()
            if hirit=="e":
                self.player1.hand.append(self.deck.pick_card())
                self.player1.print_hand()
            self.cpu.print_hand()
            self.player1.hand_value()
            self.cpu.hand_value()
            if abs((self.player1.hand_val-21))<abs((self.cpu.hand_val-21)):
                if self.player1.hand_val<=21 or (self.player1.hand_val>21 and self.cpu.hand_val>21):
                    self.player1.wins += 1
                    print(self.player1.name + " wins")
                else:
                    self.cpu.wins += 1
                    print(self.cpu.name + " wins")
            elif self.player1.hand_val==self.cpu.hand_val:
                print("It's a tie")
            else:
                if self.cpu.hand_val<=21 or (self.player1.hand_val>21 and self.cpu.hand_val>21):
                    self.cpu.wins += 1
                    print(self.cpu.name + " wins")
                else:
                    self.player1.wins += 1
                    print(self.player1.name + " wins")
            q = input("Enter \"q\" to quit ").lower()
            if q=="q":
                break
            self.player1.hand.clear()
            self.cpu.hand.clear()
        print(str(self.player1.name) + " won " + str(self.player1.wins) + " times")
        print(str(self.cpu.name) + " won " + str(self.cpu.wins) + " times")

game = Game()
game.play_game()