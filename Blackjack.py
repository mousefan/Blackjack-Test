# Blackjack


# Importing random variables
import random

# Generate the deck itself
# a list of all the suits 
Suits = ['Clubs', 'Diamonds', 
		'Hearts', 'Spades'] 
# a list of all the ranks 
Ranks = ['Ace', '2', '3', '4', 
		'5', '6', '7', '8', 
		'9', '10', 'Jack', 'Queen', 'King'] 

# Matching all the suits with all the ranks 
deck = [f"{x} of " + y for x in Ranks for y in Suits]

dealerRecord = 0
playerRecord = 0






# Shuffle the deck
def shuffle(deck):
    return random.shuffle(deck)



# The rest of the game takes place inside of this function
def hand(dealerRecord, playerRecord, deck=deck, dealerHand=[], playerHand=[]):
    deck = [f"{x} of " + y for x in Ranks for y in Suits]
    shuffle(deck)
    dealerHand = []
    playerHand = []
    
    
    
    # Adds the top card of the deck to the Dealer's hand
    def dealerDraw(dealerHand, deck):
        topCard = deck.pop(0)
        return dealerHand.append(topCard)
    
    
    
    # Same as above, but adds it to the Player's hand
    def playerDraw(playerHand, deck):
        topCard = deck.pop(0)
        return playerHand.append(topCard)
    
    
    
    # Function that runs when the player "hits." Just adds up the hand, the card is actually drawn at the decision and not here
    def playerAddHand(dealerRecord, playerHand, deck):
        print(f"You draw the {playerHand[-1]}")
        for i in range(len(playerHand)):
            if isinstance(playerHand[i], str):
                if playerHand[i][0:1] in ("K", "Q", "J"):
                    playerHand[i] = 10
                elif playerHand[i][0:1] in ("A "):
                    playerHand[i] = 11
                elif playerHand[i][0:2] in ("2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10"):
                    playerHand[i] = int(playerHand[i][0:2])
                else: print("This might be an error")
            else: playerHand[i] = int(playerHand[i])
        
        # Check if the Player's hand breaks any rules after the draw
        if sum(playerHand) > 21:
            for i in range(len(playerHand)):
                if playerHand[i] == 11:
                    playerHand[i] = 1
                    print("An Ace made you go over 21 on that draw, so it was changed to a 1.")
                    return playerDecision()
            print(f"You have {playerHand} making {sum(playerHand)}. Bust!")
            dealerRecord = dealerRecord + 1
            return endGame(playerRecord, dealerRecord)
        
        else: 
            return playerDecision()
    
    
    
    # When the Player "stands" this runs. Basically the Dealer's AI. Adds up the Dealer's hand primarily and then checks the rules at the end
    def addHand(dealerRecord, playerRecord, dealerHand, deck):
        for i in range(len(dealerHand)):
            if isinstance(dealerHand[i], str):
                if dealerHand[i][0:1] in ("K", "Q", "J"):
                    dealerHand[i] = 10
                elif dealerHand[i][0:1] in ("A "):
                    dealerHand[i] = 11
                elif dealerHand[i][0:2] in ("2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10"):
                    dealerHand[i] = int(dealerHand[i][0:2])
                else: print("This might be an error")
            else: dealerHand[i] = int(dealerHand[i])
        
       # Once the hand is added up, this part will follow the rules of Blackjack for the Dealer 
        if sum(dealerHand) < 16:
            print(f"Dealer has {dealerHand}, making {sum(dealerHand)}, less than 16")
            print("")
            dealerDraw(dealerHand, deck)
            print(f"The Dealer draws the {dealerHand[-1]}")
            return addHand(dealerRecord, playerRecord, dealerHand, deck)
        
        if sum(dealerHand) > 21:
            for i in range(len(dealerHand)):
                if dealerHand[i] == 11:
                    dealerHand[i] = 1
                    print("An Ace made the Dealer go over 21 on that draw, so it was changed to a 1.")
                    return addHand(dealerRecord, playerRecord, dealerHand, deck)
            else: 
                print(f"{dealerHand} making {sum(dealerHand)}, Dealer Busts!")
                playerRecord = playerRecord + 1
                return endGame(playerRecord, dealerRecord)
        
        else:
            if sum(dealerHand) > sum(playerHand):
                print(f"Dealer has {sum(dealerHand)} against your {sum(playerHand)}. Dealer Wins!")
                dealerRecord = dealerRecord + 1
                return endGame(playerRecord, dealerRecord)
            if sum(dealerHand) == sum(playerHand):
                print(f"Dealer has {sum(dealerHand)} against your {sum(playerHand)} It's a tie!")
                return endGame(playerRecord, dealerRecord)
            else: 
                for i in range(len(dealerHand)):
                    if dealerHand[i] == 11:
                        dealerHand[i] = 1
                        return addHand(dealerRecord, playerRecord, dealerHand, deck)
                    else:
                        print(f"Dealer has {sum(dealerHand)} against your {sum(playerHand)}. You win!")
                        playerRecord = playerRecord + 1
                        return endGame(playerRecord, dealerRecord)
    
    
    
    # Hands control over to the player and brings everything up to date. 
    def playerDecision():
        for i in range(len(playerHand)):
            if isinstance(playerHand[i], str):
                if playerHand[i][0:1] in ("K", "Q", "J"):
                    playerHand[i] = 10
                elif playerHand[i][0:1] in ("A "):
                    playerHand[i] = 11
                elif playerHand[i][0:2] in ("2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10"):
                    playerHand[i] = int(playerHand[i][0:2])
                else: print("This might be an error")
            else: playerHand[i] = int(playerHand[i])
            
        #Actual decision making
        userInput = input(f"You currently have {playerHand} making {sum(playerHand)}. Would you like to hit or stand? ")
        if userInput.lower() == "stand":
            print("")
            print(f"The Dealer's hand starts with {dealerHand}")
            return addHand(dealerRecord, playerRecord, dealerHand, deck)
        if userInput.lower() == "hit":
            print("")
            playerDraw(playerHand, deck)
            return playerAddHand(dealerRecord, playerHand, deck)
        else:
            print("That is not a valid reply. You may only hit or stand.")
            return(playerDecision())
        
        
    
    # At the end of a hand, ask the player if they want to play again
    def endGame(playerRecord, dealerRecord):
        print("")
        print(f"Current record is Dealer {dealerRecord} - You {playerRecord}.")
        print("=================================================================================================================================")
        userInput = input("Would you like to play again? ")
        if userInput.lower() == "yes" or "y" or "deal" or "go":
            return hand(dealerRecord, playerRecord)
        else: print("Type 'hand()' to play again, otherwise you are free to close this window.")
        
        
        
    # Deals the cards and hands the game off to the player
    dealerDraw(dealerHand, deck)
    playerDraw(playerHand, deck)
    dealerDraw(dealerHand, deck)
    playerDraw(playerHand, deck)
    print(f"The dealer shows the {dealerHand[0]}")
    print("")
    print(f"Your hand contains: {playerHand}")
    playerDecision()



hand(dealerRecord, playerRecord)