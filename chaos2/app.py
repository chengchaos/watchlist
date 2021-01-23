# -*- coding:utf-8 -*-

from flask import Flask, render_template
from chaos2.db.watchlist_db import get_watch_list
from chaos2.entity.user import User

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


# 对于多个模版内都需要使用的变量，我们可以使用 app.context_processor 装饰器
# 组册一个模版上下文处理函数：
# 这个函数返回的变量（以字典键值对的形式）将会统一注入到每一个模版的上下文环境中。
# 因此可以在模版中直接使用。
@app.context_processor
def inject_user():
    user = User()
    return dict(user=user)  # 需要返回字典，等同于 {'user' : user}


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


@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模版和状态码


if __name__ == "__main__":
    app.run(debug=True)
