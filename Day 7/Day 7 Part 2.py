with open('input.txt') as input:
    contents = input.readlines()

hands = []
for line in contents:
    line = line.split()
    hands.append(line)

def rank_assignment(numbers):
    #print(numbers)
    if 5 in numbers:
        return 6
    if 4 in numbers:
        return 5
    if 3 in numbers:
        if 2 in numbers:
            return 4
        return 3
    if 2 in numbers:
        counter = 0
        for number in numbers:
            if number == 2:
                counter += 1
        if counter == 2:
            return 2
        else:
            return 1
    else:
        return 0

def card_compare(card):
    if card == "A":
        return 14
    if card == "K":
        return 13
    if card == "Q":
        return 12
    if card == "J":
        return 1
    if card == "T":
        return 10
    else:
        return int(card)

def tiebreaker(hand1, hand2):
    #print(f"hand1: {hand1}, hand2: {hand2}")
    for card in range(5):
        if card_compare(hand1[card]) == card_compare(hand2[card]):
            continue
        if card_compare(hand1[card]) > card_compare(hand2[card]):
            #print("Hand1 bigger")
            return True
        if card_compare(hand1[card]) < card_compare(hand2[card]):
            #print("Hand2 bigger")
            return False


ranked_list =[]
def camel_cards_ranking (hand, bid):
    print(f"--------------start ranking------------")
    print(f"hand: {hand}")
    hand_dict = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }
    jokers = 0
    for card in hand:
        if card == "J":
            jokers += 1
            continue
        hand_dict[card] += 1
    numbers_of_card_types = []
    for amount in hand_dict.values():
        if amount > 0:
            numbers_of_card_types.append(amount)
    biggest_number = 0
    index = 0
    for i, amount in enumerate(numbers_of_card_types):
        if amount >= biggest_number:
            biggest_number = amount
            index = i
    if jokers == 5:
        numbers_of_card_types = [0]
    numbers_of_card_types[index] = numbers_of_card_types[index] + jokers
    rank = rank_assignment(numbers_of_card_types)
    #print(hand_dict)
    #print(f"ranking: {rank}")
    if not bool(ranked_list):
        print("First item")
        ranked_list.append([hand, rank, bid])
        return
    if rank > ranked_list[0][1]:
        print("Goes on top")
        ranked_list.insert(0, [hand, rank, bid])
        return
    if rank < ranked_list[-1][1]:
        print("Goes at bottom")
        ranked_list.append([hand, rank, bid])
        return
    if len(ranked_list) == 2:
        print("First middle")
        ranked_list.insert(1, [hand, rank, bid])
        return
    #print(f"smallest: {ranked_list[-1][1]}, largest: {ranked_list[0][1]}")
    if rank >= ranked_list[-1][1] and rank <= ranked_list[0][1]:
        print(f"Goes in the middle")
        #print(f"ranked_list: {ranked_list}")
        for each, item in enumerate(ranked_list):
            #print(f"item: {item} should equal {ranked_list[each]}")
            #print(f"hand: {hand} comapred to item: {item}")
            #print(f"comparing {rank} to {ranked_list[each][1]}")
            #print(f"item[1]: {item[1]}")
            if rank > item[1]:
                print(f"above {item[0]}")
                ranked_list.insert(each, [hand, rank, bid])
                return
            if rank == item[1]:
                if tiebreaker(hand, item[0]):
                    print(f"above {item[0]}")
                    ranked_list.insert(each, [hand, rank, bid])
                    return
    print("Goes at bottom")
    ranked_list.append([hand, rank, bid])






#print(hands[0][0])
#print(hands)
for hand, bid in hands:
    camel_cards_ranking(hand, bid )

#print(ranked_list)
for line in ranked_list:
    print(f"{line[0]}, {line[1]}")

counter = len(ranked_list)
total_points = 0
for hand  in ranked_list:
    total_points +=  counter * int(hand[2])
    counter -= 1
print(total_points)
