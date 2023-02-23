import pandas as pd
from random import randint

movie_json = pd.read_json("/Users/Bogruk/imdb_scrap/result.json")

m_index = randint(0, len(movie_json))

print(movie_json.loc[m_index])

