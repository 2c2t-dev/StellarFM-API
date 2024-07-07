import sanic
import requests
import sanic.response

async def currentsong(request: sanic.Request):
    req = requests.get("https://stream.stellarfm.fr/currentsong?sid=1")
    return sanic.response.text(req.text)