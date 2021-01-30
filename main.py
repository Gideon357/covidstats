import time

import tweepy
from data import Data

from flask import Flask, render_template

app = Flask(__name__)
data = Data()


@app.route("/")
def index():
    return render_template(
        "index.html",
        herd=data.getHerd(),
        vaccinations=data.getVacc(),
        casesDeaths=data.getCasesDeaths(),
    )


app.run()