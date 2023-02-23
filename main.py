import requests     
from bs4 import BeautifulSoup
import json

def collect_data():

    url = requests.get("https://www.imdb.com/chart/top/")
    soup = BeautifulSoup(url.content, "html.parser")
    movies = soup.find_all('td', class_ ='titleColumn')

    movie_data = []

    for movie in movies:
        link = 'https://www.imdb.com' + movie.find('a')['href']
        title = movie.find('a').text
        year = movie.find('span', class_='secondaryInfo').text
        rating = movie.find_next_sibling().find('strong').text
        movie_data.append({"link:" : link ,"title:": title,"year:": year,"rating:": rating})

        with open("result_1.json", "w") as file:
            json.dump(movie_data, file, ensure_ascii=False)


def main():
    collect_data()


if __name__ == "__main__":
    main()
