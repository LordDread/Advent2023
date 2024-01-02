with open('input.txt') as input:
    contents = input.readlines()

card_list = [1]*len(contents)
for amount, line in enumerate(contents):
    line = line.rstrip().split(':')
    line = line[1].split('|')
    winning_numbers = line[0].split(' ')
    numbers =  line[1].split(' ')
    number_of_wins = 0
    for number in numbers:
        if number in winning_numbers and number != '':
            number_of_wins += 1
            #print(f"winning number: {number}")
    iterator = 1
    for each_win in range(number_of_wins):
        #print(f"{card_list[amount + iterator]} += {card_list[amount]}")
        card_list[amount + iterator] += card_list[amount]
        iterator += 1

print(sum(card_list))


