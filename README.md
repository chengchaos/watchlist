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

5/ 安装 Gunicorn

```bash
(env) $ pip3 install gunicorn
```
或者使用 `--uesr` 方式安装到自己的的环境中：

```bash
pip3 install gunicorn --user
export PATH=/home/username/.local/bin:$PATH

```

6/ 运行

```bash
gunicorn -w 4 -b 127.0.0.1:4000 run:app
```

其中：

- `-w 4` 是指预定义的工作进程数为 4
- `b 127.0.0.1:4000` 指绑定的地址和短裤
- `run` 是 flask 的启动 python 文件， `app` 则是 flask 应用程序实例名

```python3
# run.py
form flask import Flask

app = Flask(__name__)
```

可以通过 `gunicorn -h` 查看配置项信息。因此通常会写成一个config.py文件来进行配置。

```python
# config.py
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

# debug = True
loglevel = 'debug'
bind = "0.0.0.0:7001"
pidfile = "log/gunicorn.pid"
pid = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'

```

启动：

```bash
gunicorn --config=config.py run:app
```


参考：

- [gunicorn部署Flask服务](https://www.jianshu.com/p/fecf15ad0c9a)

