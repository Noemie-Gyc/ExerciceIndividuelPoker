#  créer un jeu de 52 cartes générée aléatoirement.
import random


def createDeck():
    cardsType=['♠︎','♣︎','♡','♢']
    cardsValue = ['A','2','3','4','5','6','7','8','9','10','J','Q','K' ]
    deck=[]

    for t in cardsType:
        for v in cardsValue:
            # Enable the association between each element of cardsType to each element of cardsvalue in an array
            card=[t,v] 
            # Transform the array in a character chain
            card=''.join(card) 
            # Send the character chain in the deck array
            deck.append(card)
    # permet de mélanger l'ordre des cartes de manière aléatoire
    random.shuffle(deck)  
    return deck

createDeck()

# Etape 2

newDeck = ['♢Q', '♠︎3', '♢6', '♠︎A', '♠︎4', '♠︎Q', '♡4', '♠︎7', '♡3', '♣︎Q', '♡10', '♣︎10', '♢5', '♠︎5', '♣︎3', '♢10', '♠︎2', '♢8', '♣︎J', '♣︎4', '♠︎8', '♡7', '♣︎K', '♠︎J', '♣︎9', '♡9', '♡A', '♢2', '♣︎5', '♡2', '♡5', '♢J', '♢3', '♣︎8', '♡J', '♡8', '♢9', '♣︎6', '♣︎7', '♠︎6', '♢7', '♡K', '♢K', '♠︎K', '♢A', '♡Q', '♣︎A', '♢4', '♡6', '♠︎9', '♠︎10', '♣︎2']
print(len(newDeck))

def deal(cardNumber) : 
    distribution = []
    randomElement = []
    # Extract XcardNumber from deck and print it into an array
    while cardNumber > 0 : 
        randomElement = random.choice(newDeck)
        distribution.append(randomElement)
        newDeck.remove(randomElement)
        randomElement = []
        cardNumber = cardNumber-1

    return distribution


player1 = deal(2)
player2 = deal(2)


# Etape 3

def flop(tourNumber) :
    # The 5 cards on the board 
    cards = [] 
    # The cards out of the game
    burntCards=[]

    while tourNumber > 0 :
       
        if len(cards) == 0:
                cards += deal(3)          
        else :
            if len(cards) > 0 :
                cards += deal(1)
                
        burntCards += deal(1)           
        tourNumber = tourNumber - 1

    return cards, burntCards

print(flop(3))
print(len(newDeck))

# Etape 4

class Card :

    card_Types = ['♠︎','♣︎','♡','♢']
    card_Values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K' ]
    
    def __init__(self, type = 0, value = 0):
        self.type = type
        self.value = value

    def __str__(self):
        return Card.card_Values[self.value]+Card.card_Types[self.type] 
        
carte1 = Card(0, 0)
print(carte1)

class Deck : 

    def __init__(self):
        self.cards = []
        for Type in range(4):
            for Value in range(0, 13):
                cards = Card(Type, Value)
                self.cards.append(cards)
    
    def mix(self):
        random.shuffle(self.cards)

    def remove_card(self):
        return self.cards.remove()
    
    def ajouter_carte(self, card):
        self.cards.append(card)
    
    def __str__(self):
        res = []
        for cards in self.cards:
            res.append(str(cards))
        return '\n'.join(res)

deck4 = Deck()

print(deck4)

# Etape 5

