import random
from logo import logo

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def print_user_cards(user_cards):
     print("your cards are: ", user_cards, ", your total value: ", sum(user_cards))

def print_dealer_cards(dealer_cards):
     print("Dealer's cards are: ", dealer_cards, ", Dealer's total value: ", sum(dealer_cards))

def get_user_card(user_cards):
        new_card = random.choice(cards)
        user_cards.append(new_card)
        print("your new card: " , new_card)
        print_user_cards(user_cards)
        return user_cards

def checkTheWinner(user_cards,dealer_cards):
     if (sum(user_cards) == sum(dealer_cards)):
          print_dealer_cards(dealer_cards)
          print_user_cards(user_cards)
          print("Game is Draw")
     elif(sum(user_cards)> sum(dealer_cards)):
          print_dealer_cards(dealer_cards)
          print_user_cards(user_cards)
          print("you won")
     else:
          print_dealer_cards(dealer_cards)
          print_user_cards(user_cards)
          print("you lose")
     
def user_turn(user_cards):
     while(True):
        response = input ("do you want to get a another card( y or n): ")
        if (response == 'n'):
            # checkTheWinner(user_cards,dealer_cards)
            return user_cards
            # break
        elif(response == 'y'):
            user_cards = get_user_card(user_cards)
            if(sum(user_cards)>21):
                print("you lose")
                return None
        else:
            print("insert a valid input")
            
        
def dealer_turn(dealer_cards,user_cards):
     while(sum(dealer_cards)<17 and sum(dealer_cards)<=sum(user_cards)):
          print_dealer_cards(dealer_cards)
          new_card = random.choice(cards)
          print("dealer's new card: " , new_card)
          dealer_cards.append(new_card)
        #   print_dealer_cards(dealer_cards)
     if(sum(dealer_cards)>21):
          print_dealer_cards(dealer_cards)
          print("you won")
          return None
     return dealer_cards

def blackjack():
    print(logo)
    user_cards = random.sample(cards,2)
    dealer_cards = random.sample(cards,2)

    print_user_cards(user_cards)
    print("Dealers first card: ", dealer_cards[0])

    user_cards = user_turn(user_cards)
    if (user_cards == None):
         return
    dealer_cards = dealer_turn(dealer_cards,user_cards)
    if (dealer_cards == None):
         return
    
    checkTheWinner(user_cards,dealer_cards)

while(True):     
    start = input("Do you want to start the game? (y or n): ")
    if (start == 'y'):
        blackjack()
    elif (start == 'n'):
         exit()
    else:
         print("insert a valid input")

