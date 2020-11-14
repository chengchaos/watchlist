# 从 flask 包导入 Flask 类
from flask import Flask
from flask import url_for 

app = Flask(__name__)

# 使用 app.route() 装饰器来为这个函数
# 绑定对应的 URL
@app.route('/')
@app.route("/index")
def root():
    return 'Welcome to My Watchlist!'

@app.route("/hello/<name>")
def hello(name):
    print("name = "+ name)
    return u'欢迎 Watchlist!' + name

@app.route("/html") 
def htmlHello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif" />'

@app.route('/test')
def test_url_for():
    print(url_for('root')) # 输出 ：/index
    print(url_for('htmlHello')) # /html
    print(url_for('hello', name='chaos')) # /hello/chaos

    return 'Test page'

