# -*- coding:utf-8 -*-

from flask import Flask, render_template
from chaos2.db.watchlist_db import get_watch_list

app = Flask(__name__)

my_name = u"程超"
movies = [
    {"title": "MyNeighbor Totoro", "year": "1988"},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]


@app.route("/")
@app.route("/index")
def index():
    my_watch_list = get_watch_list(1)

    return render_template("index.html",
                           name=my_name,
                           movies=my_watch_list)


@app.route("/hello1")
def hello1():
    return u"还原来到我的 Watchlist！"


@app.route("/hello2")
def hello2():
    return "<h1>Hello Totoro!</h1>"


@app.route("/user/<name>")
def user_page(name):
    return "user page: %s" % name


if __name__ == "__main__":
    app.run(debug=True)
