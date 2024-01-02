#parsing data function
def parse(contents):
    games = []
    for temp_games in contents:
        temp_games = temp_games.split(':')
        for game in temp_games[1:]:
            game_data = []
            game = game.split(';')
            for round in game:
                round = round.split(',')
                round_data = {}
                for item in round:
                    item = item.split(' ')
                    round_data.update({item[2].rstrip():int(item[1])})
                #print(round_data)
                game_data.append(round_data)
            #print(game_data)
        games.append(game_data)
    return games

#solution function
def dict_color_count(game):
    color_dict = {'red': 1, 'green': 1, 'blue': 1}
    for round in game:
        #print(f'round: {round}')
        for color in ['red', 'green', 'blue']:
            if color in round and round[color] > color_dict[color]:
                color_dict[color] = round[color]
    return color_dict

with open('input.txt') as input:
    contents = input.readlines()

games = parse(contents)

power_scouter = 0
for game in games:
    #print(f'game: {game}')
    result = dict_color_count(game)
    #print(f"{result}\n {result['red']} * {result['green']} * {result['blue']} = {result['red'] * result['green'] * result['blue']}")
    power_scouter += (result['red'] * result['green'] * result['blue'])

if power_scouter>9000:
    print(f"It's over 9000!\n{power_scouter}")
else:
    print(power_scouter)