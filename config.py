# import os
import gevent.monkey
import multiprocessing

gevent.monkey.patch_all()


# debug = True
loglevel = 'debug'
bind = "0.0.0.0:7001"
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
