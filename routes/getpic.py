import sanic
import sanic.response
import requests

from core.spotify import get_access_token
from core.cache import CacheManager

async def getpic(request: sanic.Request):
    cache = CacheManager()
    song = requests.get("https://stream.stellarfm.fr/currentsong?sid=1").text
    if cache.is_exist(song):
        return sanic.response.text(cache.get(song))
    else:
        access = get_access_token()
        url = ""
        headers = {
            "Authorization": f"Bearer {access}"
        }
        params = {
            "q": song,
            "type": "track",
            "market": "FR",
            "limit": 1
        }
        response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('tracks'):
                items = data.get('tracks').get('items')
                if items:
                    item = items[0]
                    images = item.get('album').get('images')
                    if images:
                        image = images[0]
                        url = image.get('url')
        if url == "":
            url = "https://i.imgur.com/8z5q5kP.png"
        cache.add(song, url)
        return sanic.response.text(url)