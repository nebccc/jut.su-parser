import json

from config import headers

import requests
from bs4 import BeautifulSoup


def select_episode():
    with open('anime_episodes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Вывод списка сезонов
    seasons = list(data.keys())
    print("Доступные сезоны:")
    for i, season in enumerate(seasons, 1):
        print(f"{i}. {season}")

    # Выбор сезона пользователем
    season_choice = int(input("Выберите номер сезона: ")) - 1
    selected_season = seasons[season_choice]

    # Вывод списка серий выбранного сезона
    episodes = data[selected_season]
    print(f"Серии {selected_season}:")
    for i, episode in enumerate(episodes, 1):
        print(f"{i}. {episode['name']}")

    # Выбор серии пользователем
    episode_choice = int(input("Выберите номер серии: ")) - 1
    selected_episode = episodes[episode_choice]

    # Получение ссылки на видео
    url = selected_episode['url']

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')
    video_element = soup.find('video', id='my-player')

    if video_element:
        # Находим первый элемент <source> внутри элемента <video>
        source_element = video_element.find('source')
        if source_element:
            # Получаем ссылку на видео из атрибута src
            video_url = source_element['src']
            return video_url
        else:
            return None
    else:
        return None
