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

