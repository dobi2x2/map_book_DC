users:list=[
    {'name': 'Dobrawa','location':'Warszawa','posts':100},
    {'name': 'Patrycja','location':'Kutno','posts':200},
    {'name': 'Maja','location':'Inowrocław','posts':300},
    {'name': 'Mateusz','location':'Poznań','posts':400},
]

import folium
import requests
from bs4 import BeautifulSoup

#https://pl.wikipedia.org/wiki/Przybys%C5%82awice_(wojew%C3%B3dztwo_lubelskie)

def get_coordinates(city: str)->list:

    url=f'https://pl.wikipedia.org/wiki/{city}'
    response=requests.get(url).text
    response_html = BeautifulSoup(response, 'html.parser')
    longitude=float(response_html.select('.longitude')[1].text. replace(',','.'))
    latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    return [latitude, longitude]


def get_mapa(users_data: list)-> None:
    mapa = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users:
        coordinates=get_coordinates(user['location'])

        folium.Marker(
            location=(coordinates[0],coordinates[1]),
            popup=(f'Twój znajomy {user["name"]} <br/> miejscowość: {user['location']} <br/> opublikował {user["posts"]} postów.')).add_to(mapa)
    mapa.save('mapa.html')