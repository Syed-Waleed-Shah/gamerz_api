import json

    


def loadJson(filePath: str):
    with open(filePath, 'r') as file:
        rawjsonString = file.read()
        return json.loads(rawjsonString)


def create_tournament():
    data = loadJson('tournament-v1.1.json')
    # Ask user to select game (pubg, bgmi, pubgm)
    while True:

        print('SELECT GAME')
        for i in range(len(data)):
            game = data[i]['name']
            print(f'{i+1}) {game}')
        choice = input('choice:')
        selected_game = data[int(choice)-1]

        # Ask user to select game type (solo, duo, squad)
        print('SELECT GAME TYPE')
        game_types = selected_game['game_type']
        for i in range(len(game_types)):
            game_type = game_types[i]['type']
            print(f'{i+1}) {game_type}')
        choice = input('choice:')
        selected_game_type = game_types[int(choice)-1]


        # Ask user to select num of participants
        prefix = 'Players'
        if selected_game_type['type'] == 'DUO': prefix='Teams'
        elif selected_game_type['type'] == 'SQUAD': prefix='Squads'
        print('SELECT NUM OF PARTICIPANTS')
        tournaments = selected_game_type['tournaments']
        for i in range(len(tournaments)):
            participants = tournaments[i]['teams']
            print(f'{i+1}) {participants} {prefix}')
        choice = input('choice:')
        selected_tournament = tournaments[int(choice)-1]



        # # Ask user to select type of tournament
        # tournament_types = selected_tournament['tournament_types']
        # for i in range(len(tournament_types)):
        #     tournament_type_name = tournament_types[i]['name']
        #     print(f'{i+1}) {tournament_type_name}')
        # choice = input('choice:')
        # selected_tournament_type = tournament_types[int(choice)-1]
        print('-'*50)
        print('CONGRATS TOURNAMENTS CREATED')
        print('-'*50)
        tournament_types = selected_tournament['tournament_types']
        for i in range(len(tournament_types)):
            tournament_type_name = tournament_types[i]['name']
            print(f'>>> {tournament_type_name} <<<')
            print('Number of groups: ', tournament_types[i]['total_groups'])
            print('Total matches: ', tournament_types[i]['total_matches'])
            print('Details & Help')
            print(tournament_types[i]['info'])
            print('_'*50)
            


create_tournament()