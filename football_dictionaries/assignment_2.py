def players_by_position(squads_list):
    players_dict = {}
    players = players_as_dictionaries(squads_list)
    
    for player in players:
        position = player['position']
        if position not in players_dict:
            players_dict[position] = []
        players_dict[position].append(player)
    
    return players_dict
