# 一个 flask tutorial

1/ 先克隆到本地

2/ 创建 env 环境

使用下面的命令创建虚拟环境，最后一个参数是虚拟环境的名称，这里就是 env.

```bash
$ python3 -m venv env

```

创建完成以后，会在当前目录中创建一个包含 Python 解释器环境的虚拟环境目录，名称及时之前写的 env。

Unix 系统可以使用以下命令激活虚拟环境，成功会在提示符前现实 `(env)`:

```bash
$ . env/bin/activate
(env) $
```

Windows 则执行 activate 命令进入，deactivate 退出：

```bat
> env\Scripts\activate

```

3/ 安装 Flask

```bash
(env) $ pip3 install flask
```

4/ 运行

```bash
(env) $ flask run
```

## flask-restful

安装：

```bash
 pip install-flask-restful
```

如果使用 flask-restful，那么定义视图函数的时候，就要继承自 `flask_restful.Resource` 类，然后再根据当前情求的 method 来定义相应的方法。比如期望客户端使用 get 方法发送过来的情求，那么就定义一个 get 方法。类似 MethodView：

```python
from flask import Flask, render_template, url_for
from flask_resultful import Api, Resource

app = Flask(__name__)
# 用 Api 来绑定 app
api = Api(app)

class IndexView(Resource):
    def get(self):
        return {"username": "chengchao"}

api.add_resource(IndexView, "/", endpoint="index")

```

参考：

- [https://www.cnblogs.com/donghaoblogs/p/10389696.html](https://www.cnblogs.com/donghaoblogs/p/10389696.html)
- [http://www.pythondoc.com/Flask-RESTful/quickstart.html](http://www.pythondoc.com/Flask-RESTful/quickstart.html)