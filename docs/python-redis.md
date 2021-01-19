# Python-redis


## redis 连接

redis提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py

redis连接实例是线程安全的，可以直接将redis连接实例设置为一个全局变量，直接使用。如果需要另一个Redis实例（or Redis数据库）时，就需要重新创建redis连接实例来获取一个新的连接。同理，python的redis没有实现select命令。

## 安装 redis

```bash
pip3 install redis
```

连接 redis，加上 `decode_responses=True`，写入的键值对中的 valu e为 str 类型，不加这个参数写入的则为字节类型。

```python
import redis

r = redis.Redis(host='localhost', port=6379,decode_responses=True)
r.set("name", "chengchao")
print(r['name'])
print(r.get('name'))
print(type(r.get('name')))
```

## 连接池

redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池

```python
# -*- coding:utf-8 -*-
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

r.set('gender', 'male')
print(r.get('gender'))

```

参考：

- [使用python来操作redis用法详解](https://www.jianshu.com/p/2639549bedc8)
- [https://github.com/andymccurdy/redis-py](https://github.com/andymccurdy/redis-py)
