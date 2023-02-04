def main():
    about_me = {
        'full_name' : 'Harrison Guy',
        'student_id' : 10297051,
        'pizza_toppings' : [
            'chicken',
            'oNIon',
            'HAM'
        ],
        'movies' : [
            {
                'title' : 'Oldboy(2003)',
                'genre' : ['action', 'drama', 'mystery']
            },
            {
                'title' : 'Parasite',
                'genre' : ['drama', 'thriller']
            }
        ] 
    }
    
    about_me['movies'].append({'title' : 'Moon', 'genre' : ['drama','mystery', 'sci-fi']}) 
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('broccoli','SPINACH'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me, )

def print_student_name_and_id(about_me):
    student_name = about_me['full_name']
    split_student_name = student_name.split(" ")
    first_name = split_student_name[0]
    #last_name not used but felt useful
    last_name = split_student_name[-1]
    student_id = about_me['student_id']
    print(f'My name is {student_name} but you can call me Sir {first_name}.\nMy student ID is {student_id}.')
    return

def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    for i,p in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = p.lower()
    about_me['pizza_toppings'].sort()        
    return

def print_pizza_toppings(about_me):
    print('My favourite pizza toppings are:')
    for p in about_me['pizza_toppings']:
        print(f'- {p}')
    return

def print_movie_genres(about_me):
    #I had to use set() because I listed all the genre for the movies and did not want it to list reapting genre
    genres = set()
    for movie in about_me['movies']:
        for genre in movie['genre']:
            genres.add(genre)
    # made it into a list so I can add then "and " at the end 
    genres = list(genres)
    #adds "and " before printing the last genre
    if len(genres) > 1:
        genres[-1] = "and " + genres[-1]    
    print('I like to watch', *genres, 'movies.', sep=", ")
    return 

def print_movie_titles(movie_list):
    movie_title = []
    for t in movie_list['movies']:
        movie_title.append(t['title'])
    movie_title = [t['title'].title() for t in movie_list['movies']]
    if len(movie_title) > 1:
        movie_title[-1] = "and " + movie_title[-1]
    print("Some of my favourite movies are", ", ".join(movie_title), end=".\n")
    return

if __name__ == '__main__':
    main()


















"""
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
    
    
    
    
    
    
    



    return


if __name__ == '__main__':
    main()
    """