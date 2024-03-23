import re

from config import headers

import aiohttp
import aiofiles

async def download_video(video_url, filename):

    match = re.search(r'\bhash=(\w+)&hash2=(\w+)\b', video_url)
    if match:
        hash1 = match.group(1)
        hash2 = match.group(2)

        # Параметры для загрузки видео
        params = {
            'hash1': hash1,
            'hash2': hash2,
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(video_url, headers=headers, params=params, raise_for_status=True) as response:
                if response.status == 200:
                    async with aiofiles.open(filename, "wb") as f:
                        async for chunk in response.content.iter_any():
                            await f.write(chunk)
                    print("Видео успешно скачано и сохранено как", filename)
                else:
                    print("Ошибка при загрузке видео. Код состояния:", response.status)