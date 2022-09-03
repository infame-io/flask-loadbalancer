import requests

from random import choice
from flask import Flask, render_template

BASE_URL = "http://127.0.0.1"

AVAILABLE_PORTS = [
    "8080",
    "8081",
    "8082"
  ]

app = Flask(__name__)


@app.route("/")
def entrypoint():
    random_port = choice(AVAILABLE_PORTS)
    url = "{}:{}/".format(BASE_URL, random_port)

    response = requests.get(url)
    response.raise_for_status()

    return render_template('index.html', content=response.content.decode("utf-8"), server_version=response.headers.get("Server"))


if __name__ == "__main__":
    app.run()
