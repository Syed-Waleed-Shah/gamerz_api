from math import ceil, floor
import json
games = [
    {
    'name':'PUBGM', 
    'players':100
}, 
 {
    'name':'BGMI', 
    'players':100
}, 
{
    'name':'PUBGM Lite', 
    'players':60
}
]
game_types = [
  {'type':'SOLO', 'players_per_team':1, 'team_name': 'Players'},
  {'type':'DUO', 'players_per_team':2, 'team_name': 'Teams'},
  {'type':'SQUAD', 'players_per_team':4, 'team_name': 'Squads'},
]



def knockout_info(game_type:dict, game:dict, total_groups:int):
    team = game_type['team_name']

    qualifers_from_each_group = floor((game['players']/game_type['players_per_team'])/total_groups)
    total_final_qualifier = qualifers_from_each_group * total_groups

    return  f"""
    In this tournament there will be {total_groups} groups. In the first knockout stage 1 game will be played in each group.
    After completing all {total_groups} group stage matches top {qualifers_from_each_group} {team} from each group will qualify for the final match.
    In the final match {total_final_qualifier} {team} will play 1 game against each other.
    This final match will decide the winners of this tournament!!    
    """

def scrim_info(game_type:dict, game:dict, total_groups:int):
    team = game_type['team_name']
    total_group_matches = total_groups * 3
    qualifers_from_each_group = floor((game['players']/game_type['players_per_team'])/total_groups)
    total_final_qualifier = qualifers_from_each_group * total_groups
    return  f"""
    1) QUALIFIERS ROUND
    In this round, there will be {total_groups} groups. In each group 3 matches will be played. After playing all {total_group_matches} group matches
    {qualifers_from_each_group} {team} from each group will qualify for the FINALS!!
    2) FINALS
    All {total_final_qualifier} qualified {team} will play 2 matches in the finals. These final matches will decide the winners of the tournament!!
    """

def grand_tournament_info(game_type:dict, game:dict, total_groups:int):
    team = game_type['team_name']
    total_group_matches = total_groups * 5
    total_semifinal_groups = ceil(total_groups/2)
    total_semifinal_matches = total_semifinal_groups * 3
    
    semifinal_qualifers_from_each_group = floor(((game['players']/game_type['players_per_team'])*total_semifinal_groups)/total_groups)
    total_semifinal_qualifiers = semifinal_qualifers_from_each_group * total_groups

    finals_qualifers_from_each_group = floor((game['players']/game_type['players_per_team'])/total_semifinal_groups)
    # Exceptional case
    if total_semifinal_groups == 1 :
        finals_qualifers_from_each_group = floor(finals_qualifers_from_each_group/2)
    total_final_qualifier = finals_qualifers_from_each_group * total_semifinal_groups
    

    return  f"""
    1) QUALIFIERS ROUND
    In this round. there will be {total_groups} groups. In each group 5 matches will be played. After playing all {total_group_matches} matches, {semifinal_qualifers_from_each_group} {team}
    from each group will qualify for the SEMIFINALS ROUND !!
    2) SEMIFINALS ROUND
    In this round, all {total_semifinal_qualifiers} qualified {team} will be distributed in {total_semifinal_groups} groups. Now, 3 matches will be played in each group.
    After completing all {total_semifinal_matches} matches, {finals_qualifers_from_each_group} {team} from each group will qualify for the FINALS!!
    3) FINALS
    All the {total_final_qualifier} qualified {team} wil play 2 matches in the finals. These final matches will decide the winners of the tournament!!
    """




def create_tournament_file(version:str):
    info = []
    game_dict = {}
    for game in games:
        game_dict = game
        game_types_list = []
        for game_type in game_types:
            type = {'type':game_type['type']}
            tournaments = []
            for i in range(2,11):
                tournament = {}
                tournament['teams'] = int(i * game['players']/(game_type['players_per_team']))
                tournament_types = []
                knockout = {'name':'knockout', 'total_groups': i, 'total_matches':i + 1, 'info':knockout_info(game_type, game, i)}
                scrim = {'name':'scrim', 'total_groups': i, 'total_matches':(i*3) + 2, 'info':scrim_info(game_type, game, i)}
                grand_tournament = {'name':'grand tournament', 'total_groups': i, 'total_matches':(i*5) + (floor(i/2) * 3 )+ 2, 'info':grand_tournament_info(game_type, game, i)}
                tournament_types.append(knockout)
                tournament_types.append(scrim)
                tournament_types.append(grand_tournament)

                tournament['tournament_types'] = tournament_types
                tournaments.append(tournament)
          

            type['tournaments'] = tournaments

            game_types_list.append(type)
        game_dict['game_type'] = game_types_list
        info.append(game_dict)

    json_info = json.dumps(info, indent=2)
    with open(f'tournament-v{version}.json', 'w') as file:
        file.write(json_info)
        file.flush()
        print(f'tournament file created : version {version}')





create_tournament_file('1.1')


