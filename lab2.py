def main():

    hockey_team = {
        'name' : 'Maple Leafs',
        'city' : 'Toronto',
        'players' : [
            'matthews',
            'marner',
            'nylander'
        ],
        'games' : [
            {
                'oppenent' : 'Canadiens',
                'goals for' : 6,
                'goals against' :2,
            },
             {
                'oppenent' : 'Ottawa',
                'goals for' : 2,
                'goals against' :3,
            }
        ]
    }
    
    hockey_team['games'].append({'opponent' : 'Boston', 'goals for' : 8, 'goals against' : 0,})
    print_team_info(hockey_team)
    add_players(hockey_team, ('gi','re','en'))
    print_team_info(hockey_team)
    print_opponents(hockey_team['games'])
    
    return

def print_opponents(team):
    opponents = []
    for g in team['games']:
        opponents.append(g['oppoent'])
    opponents = [g['opponent'].title() for g in team['games']]
    print(', '.join(opponents), end='.\n')

    return

def add_players(team, new_players):
    team['players'].extend(new_players)
    team['players'].sort()
    for i,p in enumerate(team['players']):
        team['players'][i] = p.capitalize()

def print_team_info(team):
    team_name = team['name'].title()
    team_city = team['city'].capitalize()
    print(f'{team_name} {team_city}')
    for p in team['players']:
        print(f'- {p.capitalize()}')
    
    
    
    
    
    
    
    about_me = {
        'full_name' : 'Harrison Guy',
        'student_id' : 10297051,
        'pizza_toppings' : [
            'chicken',
            'ham',
            'onion'
        ],
        'movies' : [
            {
                'title' : '',
                'genre' : ''
            },
            {
                'title' : '',
                'genre' : ''
            }
        ] 
    }
    about_me['movies'].append({'title' : '', 'genre' : ''}) 


    return


if __name__ == '__main__':
    main()