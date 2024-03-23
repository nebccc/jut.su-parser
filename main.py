import asyncio

import jutsu
import episode_selection
from downloader import download_video

async def main():
    url = input("Enter the link: ")

    jutsu.fetch_anime_episodes(url)

    video_link = episode_selection.select_episode()

    if video_link:
        file_name = 'video.mp4'
        await download_video(video_link, file_name)
    else:
        print("Ссылка на видео не найдена.")

if __name__ == "__main__":
    asyncio.run(main())