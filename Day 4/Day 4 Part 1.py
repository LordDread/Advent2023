with open('input.txt') as input:
    contents = input.readlines()

total_points = 0

for line in contents:
    #print(line.rstrip().split(':'))
    line = line.rstrip().split(':')
    line = line[1].split('|')
    winning_numbers = line[0].split(' ')
    numbers =  line[1].split(' ')
    number_of_wins = -1
    for number in numbers:
        if number in winning_numbers and number != '':
            #print(f"winning number: {number}")
            number_of_wins += 1
    if number_of_wins >= 0:
        #print(f"wins: {number_of_wins} with {pow(2, number_of_wins)} points")
        total_points += pow(2,number_of_wins)


print(total_points)


