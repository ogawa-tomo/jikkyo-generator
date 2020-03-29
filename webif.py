from flask import Flask, render_template, request, redirect, url_for
from generator.kurashiki import *


app = Flask(__name__)
title = "実況ジェネレータ"


class Settings(object):

    def __init__(self, scorer, team):
        self.scorer = scorer
        # self.assist = assist
        self.team = team


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def post():
    if request.method == "POST":

        scorer = request.form["scorer"]
        # assist = request.form["assist"]
        team = request.form["team"]

        settings = Settings(scorer, team)
        result = make_jikkyo(scorer, team)

        return render_template("index.html", result=result, settings=settings)


if __name__ == "__main__":
    app.run()
