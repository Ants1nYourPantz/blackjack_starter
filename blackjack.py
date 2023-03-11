import random
print("Welcome to Blackjack! Take a seat!")
print("""
        The rules of the game are as follows:

        1. The goal of blackjack is to beat the dealer's hand without going over 21.
        2. To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.  
        3. If you go over 21 you bust, and the dealer wins regardless of the dealer's hand. 
        4. If you are dealt 21 from the start (Ace & 10), you got a blackjack.

        ENJOY AND GOOD LUCK!
    """)

print("Dealing cards...")
class Deck:
    def __init__(self):
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        names = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, name) for suit in suits for name in names]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)


class Game:

    def __init__(self):
        self.deck = None

    def play(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hand = []
        self.dealer = []
        
        for card in range(2):
            self.dealer.append(self.deck.deal())
        for i in range(1, len(self.dealer)):
            card = self.dealer[i]
            print("=" * 50)
            statement = print(f"The dealer has {card.name} of {card.suit}")
            print("=" * 50)
        for crd in range(2):
            self.hand.append(self.deck.deal())
        for card in self.hand:
            print(f"--- {card.name} of {card.suit} ---")
        print(f"Your first cards are a total of {sum(crd.value for crd in self.hand)}")
        print("=" * 50)

        

        while True:
            if sum(crd.value for crd in self.hand) == 21 and len(self.hand) == 2:
                print("Blackjack!")
                break

            elif sum(crd.value for crd in self.hand) > 21 and len(self.hand) == 2:
                print("Bust, dealer wins!")
                break

            elif sum(crd.value for crd in self.hand) <= 21:
                answer = input("Would you like to Hit or Stand? ").lower()

                if answer == "hit":
                    self.hand.append(self.deck.deal())
                    new_card = self.hand[-1]
                    print(f"--- {new_card.name} of {new_card.suit} ---")
                    print(f"You now have a total of {sum(crd.value for crd in self.hand)} in your hand.")
                    print("=" * 50)
                    if sum(crd.value for crd in self.hand) > 21:
                        print("Bust, dealer wins!")
                                    
                elif answer == "stand":
                    print(f"Your card total is {sum(crd.value for crd in self.hand)}. ")
                    print(f"Dealer's total is {sum(crd.value for crd in self.dealer)}. ")

                    if sum(card.value for card in self.dealer) < 17:
                        self.dealer.append(self.deck.deal())
                        dealer_card = self.dealer[-1]
                        print(f"--- {dealer_card.name} of {dealer_card.suit} ---")
                        print(f"The dealer now has a total of {sum(crd.value for crd in self.dealer)}.")


                    if sum(crd.value for crd in self.dealer) > sum(crd.value for crd in self.hand) and sum(crd.value for crd in self.dealer) <= 21:
                        print("Dealer wins!")
                        
                        

                    elif sum(crd.value for crd in self.dealer) < sum(crd.value for crd in self.hand) and sum(crd.value for crd in self.hand) <= 21:
                        print("You win!")
                        

                    elif sum(crd.value for crd in self.dealer) > 21:
                        print("Dealer busts, you win!")
                        

                    elif sum(crd.value for crd in self.dealer) == sum(crd.value for crd in self.hand):
                        print("It's a tie!")
                        
                        
                    else:
                        print("Please enter either 'hit' or'stand'. ")
                        continue

                    again = input("Would you like to play again? Yes/No ").lower()
                    if again == "yes":
                        self.play()
                    else:
                        print("Thanks for playing!")
                        break

            else:
                again = input("Would you like to play again? Yes/No ").lower()
                if again == "yes":
                    self.play()
                else:
                    print("Thanks for playing!")
                    break


                                
 
class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

        if isinstance(name, int):
            self.value = name
        elif name == 'Ace':
            self.value = 11
        else:
            self.value = 10

    def __add__(self, other):
        return self.value + other.value
       

game = Game()
game.play()