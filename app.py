# -*- coding:utf-8 -*-
# 从 flask 包导入 Flask 类
from flask import Flask, render_template
from flask import url_for
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

name = "Grey Li"
movies = [
    {'title': "My Neighbor Totoro", 'year': '1988'},
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


# 使用 app.route() 装饰器来为这个函数
# 绑定对应的 URL


@app.route('/')
@app.route("/index")
def root():
    return render_template('index.html', name=name, movies=movies)


@app.route("/hello/<name>")
def hello(name):
    print("name = " + name)
    return u'欢迎 Watchlist!' + name


@app.route("/html")
def htmlHello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif" />'


@app.route('/test')
def test_url_for():
    print(url_for('root'))  # 输出 ：/index
    print(url_for('htmlHello'))  # /html
    print(url_for('hello', name='chaos'))  # /hello/chaos

    return 'Test page'


class MyView(Resource):
    def get(self, name):
        return {'username': name}


api.add_resource(MyView, "/my/<string:name>", endpoint="my")


if __name__ == "__main__":
    app.run(debug=True)
