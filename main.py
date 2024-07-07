import sanic
import dotenv

from routes.currentsong import currentsong
from routes.getpic import getpic

dotenv.load_dotenv(".env")

app = sanic.Sanic("StellarFM-API")

app.add_route(currentsong, "/currentsong", methods=["GET"])
app.add_route(getpic, "/getpic", methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, workers=4, access_log=True)