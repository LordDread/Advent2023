with open('input.txt') as input:
    contents = input.readlines()

####    cut off game number from start of list
games = []
for game in contents:
    game = game.split(':')
    games.append(game[1])

####    split each game into seperate pulls
temp_games = [] # used to temporaliy hold each game as it is being split and compiled into new list
for game in games:
    game = game.split(';')
    temp_games.append(game)

####    Break each pull into digits and colors
games = temp_games
temp_games = []
for game in games:
    temp_number_or_cube = []
    for number_or_cube in game:
        number_or_cube=number_or_cube[1:].split(' ') # remove troublesome empty element created from split
        temp_number_or_cube.append(number_or_cube)
    temp_games.append(temp_number_or_cube)
games = temp_games

####    function used to check if the number and color of cubes does not exceed limits
def color_check(rgb, digi):
    if rgb[0] == 'r' and digi > 12:
        print('too many red cubes')
        return True
    if rgb[0] == 'g' and digi > 13:
        print('too many green cubes')
        return True
    if rgb[0] == 'b' and digi > 14:
        print('too many blue cubes')
        return True
    else:
        return False

possible_game = True
game_counter = 0
for index, game in enumerate(games, start = 1):         # Iterates across each game counting up starting at 1
    game_counter = game_counter + index                 # counts up all games to be subtracted from
    print(f'Game {index}:')
    for counter, pull in enumerate(game):               # Iterates across each pull from the bag of each game
        if possible_game == False and counter == 0:
            possible_game = True
        if possible_game == False:
            possible_game = True
            break
        print(pull)
        for each, item in enumerate(pull):              # iterates across each number/color of cubes in current pull
            if item.isdigit() and int(item) > 12:
                print(f'{pull[each+1]} {item}')
                if color_check(pull[each+1],int(item)):
                    game_counter = game_counter - index # subtracts impossible games
                    possible_game = False
                    break

print(game_counter)                                     # prints final total of possible games's numbers together