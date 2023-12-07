# Don't even ask me about this code, I hate it
f = open("day7.txt", encoding='utf8')

cards = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

lines = [line.replace("\n","") for line in f if line != "\n"]

#print(lines)
hands = [line.split(" ")[0] for line in lines]
bets = [line.split(" ")[1] for line in lines]

hand_types= []
hand_types_words = ["high card","one pair","two pairs","three of a kind","full house","four of a kind","five of a kind"]

for hand in hands:
    #check if hand is five of a kind
    if all(card == hand[0] for card in hand):
        hand_types.append(7)
        continue
    #check if hand is high card
    different_card = []
    for card in hand:
        if card not in different_card:
            different_card.append(card)
    if len(different_card) == 5:
        hand_types.append(1)
        continue
    #check if hand is four of a kind
    kind4 = False
    for card in hand:
        if(hand.count(card) == 4):
            hand_types.append(6)
            kind4 = True
            break
    if kind4:
        continue
    #check if hand is full house
    kind3 = False
    kind2 = False
    for card in hand:
        if(hand.count(card) == 3):
            kind3 = True
        elif(hand.count(card) == 2):
            kind2 = True
    if kind3 and kind2:
        hand_types.append(5)
        continue
    #check if hand is three of a kind
    if kind3:
        hand_types.append(4)
        continue
    #check if hand is two pairs
    if kind2:
        #check if hand is 2 pairs or 1 pair
        kind22 = False
        card1 = ""
        for card in hand:
            if(hand.count(card) == 2):
                if card1 == "":
                    card1 = card
                elif card1 != card:
                    kind22 = True
                    break
        if kind22:
            hand_types.append(3)
            continue
        else:
            hand_types.append(2)
            continue


hand_types, hands, bets = zip(*sorted(zip(hand_types, hands, bets)))

hand_types = list(hand_types)
hands = list(hands)
bets = list(bets)

i = 0
while i < len(hand_types)-1:
    #print("fuck")
    if hand_types[i] == hand_types[i+1]:
        swapped = False
        for j in range(len(hands[i])):
            if(cards.index(hands[i][j]) < cards.index(hands[i+1][j])):
                break
            elif (cards.index(hands[i][j]) >cards.index(hands[i+1][j])): 
                hands[i], hands[i+1] = hands[i+1], hands[i]
                bets[i], bets[i+1] = bets[i+1], bets[i]
                i = 0
                swapped = True
                break
        if swapped:
            continue
    i+=1

sum_of_bets = 0
for i in range(len(hands)):
    sum_of_bets += (int(bets[i])*(i+1))

print("Part 1: ",sum_of_bets)

f = open("day7.txt", encoding='utf8')

cards = ["J","2","3","4","5","6","7","8","9","T","Q","K","A"]

lines = [line.replace("\n","") for line in f if line != "\n"]


hands = [line.split(" ")[0] for line in lines]
bets = [line.split(" ")[1] for line in lines]

hand_types= []
hand_types_words = ["high card","one pair","two pairs","three of a kind","full house","four of a kind","five of a kind"]

for hand in hands:
    
    test_hand = hand.replace("J","")
    if all(card == test_hand[0] for card in test_hand):
        hand_types.append(7)
        continue

    if(len(test_hand) == 5):
        #check if hand is high card
        different_card = []
        for card in hand:
            if card not in different_card:
                different_card.append(card)
        if len(different_card) == 5:
            hand_types.append(1)
            continue
        #check if hand is four of a kind
        kind4 = False
        for card in hand:
            if(hand.count(card) == 4):
                hand_types.append(6)
                kind4 = True
                break
        if kind4:
            continue
        #check if hand is full house
        kind3 = False
        kind2 = False
        for card in hand:
            if(hand.count(card) == 3):
                kind3 = True
            elif(hand.count(card) == 2):
                kind2 = True
        if kind3 and kind2:
            hand_types.append(5)
            continue
        #check if hand is three of a kind
        if kind3:
            hand_types.append(4)
            continue
        #check if hand is two pairs
        if kind2:
            #check if hand is 2 pairs or 1 pair
            kind22 = False
            card1 = ""
            for card in hand:
                if(hand.count(card) == 2):
                    if card1 == "":
                        card1 = card
                    elif card1 != card:
                        kind22 = True
                        break
            if kind22:
                hand_types.append(3)
                continue
            else:
                hand_types.append(2)
                continue
    elif len(test_hand) == 4:
        different_card = []
        for card in test_hand:
            if card not in different_card:
                different_card.append(card)
        if len(different_card) == 4:
            hand_types.append(2)
            continue
        #3 kind
        kind3 = False
        for card in test_hand:
            if(test_hand.count(card) == 3):
                kind3 = True
                break
        if kind3:
            hand_types.append(6)
            continue
        # 2 pairs
        kind2 = False
        card1 = ""
        for card in test_hand:
            if(test_hand.count(card) == 2):
                card1 = card
                kind2 = True
                break
        if kind2:
            kind22 = False
            for card in test_hand:
                if(test_hand.count(card) == 2 and card != card1):
                    kind22 = True
                    break
            if kind22:
                hand_types.append(5)
                continue
            else:
                hand_types.append(4)
                continue
        
            
    elif len(test_hand) == 3:
        
        different_card = []
        for card in test_hand:
            if card not in different_card:
                different_card.append(card)
        if len(different_card) == 3:
            hand_types.append(4)
            continue

        kind2 = False
        for card in test_hand:
            if(test_hand.count(card) == 2):
                kind2 = True
                break
        if kind2:
            hand_types.append(6)
            continue
    elif len(test_hand) == 2:
        hand_types.append(6)
        continue
    else:
        hand_types.append(7)

hand_types, hands, bets = zip(*sorted(zip(hand_types, hands, bets)))

hand_types = list(hand_types)
hands = list(hands)
bets = list(bets)

i = 0
while i < len(hand_types)-1:
    #print("fuck")
    if hand_types[i] == hand_types[i+1]:
        swapped = False
        for j in range(len(hands[i])):
            if(cards.index(hands[i][j]) < cards.index(hands[i+1][j])):
                break
            elif (cards.index(hands[i][j]) >cards.index(hands[i+1][j])): 
                hands[i], hands[i+1] = hands[i+1], hands[i]
                bets[i], bets[i+1] = bets[i+1], bets[i]
                i = 0
                swapped = True
                break
        if swapped:
            continue
    i+=1

sum_of_bets = 0
for i in range(len(hands)):
    sum_of_bets += (int(bets[i])*(i+1))

print("Part 2: ",sum_of_bets)