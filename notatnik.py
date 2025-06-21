class User:
    def __init__(self, name: str, surname: str, location: str, posts: str,):
        self.name=name
        self.surname=surname
        self.location=location
        self.posts=posts
        self.coordinates=self.get_coordinates()

    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup

        url = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(url).text
        response_html = BeautifulSoup(response, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        return [latitude, longitude]









user_1=User(name='aaa', surname='bbb', location='Warszawa', posts='ddd')
print(user_1.name, user_1.surname, user_1.location, user_1.posts, user_1.coordinates)
user_2=User(name='acaa', surname='bcbb', location='Kraków', posts='cddd')
print(user_2.name, user_2.surname, user_2.location, user_2.posts, user_2.coordinates)