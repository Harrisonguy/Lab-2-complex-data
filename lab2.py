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
                'title' : 'oldboy(2003)',
                'genre' : ['action', 'drama', 'mystery']
            },
            {
                'title' : 'parasite',
                'genre' : ['drama', 'thriller']
            }
        ] 
    }

    about_me['movies'].append({'title' : 'moon', 'genre' : ['drama','mystery', 'sci-fi']}) 
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('broccoli','SPINACH'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)

def print_student_name_and_id(about_me):
    student_name = about_me['full_name']
    split_student_name = student_name.split(" ")
    first_name = split_student_name[0]
    last_name = split_student_name[-1] #last_name not used but felt useful
    student_id = about_me['student_id']
    print(f'My name is {student_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.\n')
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
    print()
    return

def print_movie_genres(about_me):
    genres = []
    for movie in about_me['movies']:
        for genre in movie['genre']:
            genres.append(genre)
    #removes duplicates
    genres = list(set(genres))
    #adds "and " before printing the last genre
    if len(genres) > 1:
        genres[-1] = "and " + genres[-1]    
    print('I like to watch', ", ".join(genres), end=" movies.\n")
    print()
    return 

def print_movie_titles(movie_list):
    movie_title = []
    for t in movie_list['movies']:
        movie_title.append(t['title'])
    movie_title = [t['title'].title() for t in movie_list['movies']]
    #adds "and " before the last movie title
    if len(movie_title) > 1:
        movie_title[-1] = "and " + movie_title[-1]
    print("Some of my favourite movies are", ", ".join(movie_title), end="!\n")
    return

if __name__ == '__main__':
    main()
