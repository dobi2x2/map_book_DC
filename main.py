

users:list=[
    {'name': 'Dobrawa','location':'Warszawa','posts':100},
    {'name': 'Patrycja','location':'Kutno','posts':200},
    {'name': 'Maja','location':'Inowrocław','posts':300},
    {'name': 'Mateusz','location':'Żeronice','posts':400},
]


def get_user_info(users_data:list)-> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} postów.')

get_user_info(users)