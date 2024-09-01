def players_by_country_and_position(squads_list):
    country_dict = {}
    players = players_as_dictionaries(squads_list)
    
    for player in players:
        country = player['country']
        position = player['position']
        
        if country not in country_dict:
            country_dict[country] = {}
        
        if position not in country_dict[country]:
            country_dict[country][position] = []
        
        country_dict[country][position].append(player)
    
    return country_dict
