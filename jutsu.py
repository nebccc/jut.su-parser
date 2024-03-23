import json

from config import headers

import requests
from bs4 import BeautifulSoup
def fetch_anime_episodes(url):

    req = requests.get(url, headers=headers).content
    soup = BeautifulSoup(req, 'html.parser')

    seasons = {}

    season_elements = soup.find_all('h2', class_='b-b-title the-anime-season center')

    for season_element in season_elements:
        season_name = season_element.text.strip()

        next_sibling = season_element.find_next_sibling()

        episodes = []

        while next_sibling and next_sibling.name != 'h2' and next_sibling.get('class') != ['b-b-title', 'the-anime-season','center']:
            if next_sibling.name == 'a':
                episode_name = next_sibling.text.strip()
                episode_url = f"https://jut.su{next_sibling.get('href')}"
                episodes.append(
                    {
                        "name": episode_name,
                        "url": episode_url
                    }
                )

            next_sibling = next_sibling.find_next_sibling()

        seasons[season_name] = episodes

    with open('anime_episodes.json', 'w', encoding='utf-8') as f:
        json.dump(seasons, f, indent=4, ensure_ascii=False)