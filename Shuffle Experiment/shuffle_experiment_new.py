def main():
    print("Please input the deck size, it has to be more than 1")
    while True:
        card_amount = int(input())
        if card_amount < 1:
            print("The inputted number is less than 1, please input a deck size that is larger than 1")
        elif card_amount == 1:
            print("The deck size cannot be 1, please input a deck size that is larger than 1")
        else:
            break
    
    #Creates the deck
    card_list = []
    for i in range(card_amount):
        card_list.append(i)
    
    #Splits the deck into two parts
    if card_amount % 2 == 0:
        card_list_left_hand = card_list[0:len(card_list)//2]
        card_list_right_hand = card_list[len(card_list)//2:len(card_list)]
    else:
        card_list_left_hand = card_list[0:len(card_list)//2+1]
        card_list_right_hand = card_list[len(card_list)//2+1:len(card_list)]

    shuffle = 0
    card_check = []
    while True:
        shuffle += 1

        #Performs the riffle shuffle
        for (i, u) in zip(card_list_left_hand, card_list_right_hand):
            card_check.append(i)
            card_check.append(u)
        #Has to add the last card from the left hand if the deck size is odd
        if card_amount % 2 != 0:
            card_check.append(card_list_left_hand[-1])

        #Checks if the deck is the same as the original deck
        if card_amount % 2 == 0:
            card_list_left_hand = card_check[:int(len(card_check)//2)]
            card_list_right_hand = card_check[int(-len(card_check)//2):]
            if card_list_left_hand == card_list[0:len(card_list)//2] and card_list_right_hand == card_list[len(card_list)//2:len(card_list)]:
                break
        else:
            card_list_left_hand = card_check[:int(len(card_check)//2+1)]
            card_list_right_hand = card_check[int(-len(card_check)//2+1):]
            if card_list_left_hand == card_list[0:len(card_list)//2+1] and card_list_right_hand == card_list[len(card_list)//2+1:len(card_list)]:
                break

        #Resets the check list
        card_check = []

    print("To return to the original deck, "+str(shuffle)+" riffle shuffles is required")

if __name__ == "__main__":
    main()